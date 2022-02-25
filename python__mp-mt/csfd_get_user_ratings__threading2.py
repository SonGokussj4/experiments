from datetime import datetime
from pprint import pprint
import concurrent.futures
import queue
import requests
from bs4 import BeautifulSoup as bs
import time
from multiprocessing import Pool, cpu_count
import threading

from csfd_functions import get_csfd_ratings_from_url, get_csfd_max_page


BASE_URL = "https://www.csfd.cz"
UZIVATEL_URL = BASE_URL + "/uzivatel/"

CONNECTIONS = 16
TIMEOUT = 5

results = []

q = queue.Queue()

def producer(page_num):
    name = threading.current_thread().name
    # for job in range(5):
    print(f'{name} thread: Starting producing {urls[i]} [{datetime.utcnow().strftime("%H:%M:%S.%f")[:-3]}]')
    q.put(urls[i])
    print(f'{name} thread: Produced {urls[i]} [{datetime.utcnow().strftime("%H:%M:%S.%f")[:-3]}]')


def consumer():
    name = threading.current_thread().name
    while True:
        url = q.get()
        print(f'C{name} thread: Starting consuming {url} [{datetime.utcnow().strftime("%H:%M:%S.%f")[:-3]}]')
        result = get_csfd_ratings_from_url(url)
        results.append(result)
        print(f'C{name} thread: Consumed {url} [{datetime.utcnow().strftime("%H:%M:%S.%f")[:-3]}]')
        q.task_done()

class Results():
    def __init__(self):
        self.vals = []

    def update_result(self, val):
        self.vals.append(val)

# results = Results()

# user_id = "78145-songokussj"
user_id = "78145"
max_page = get_csfd_max_page(user_id)
# max_page = 4
urls = [UZIVATEL_URL + user_id + f"/hodnoceni/?page={page_num}" for page_num in range(1, max_page + 1)]

start = time.time()

for i in range(1, CONNECTIONS + 1):
    t = threading.Thread(target=consumer, daemon=True, name=f"{i}").start()

for i in range(max_page):
    # q.put(urls[i])
    threading.Thread(target=producer, daemon=True, name=f"{i}", args=(i, )).start()

q.join()

end = time.time() - start

print('Done')

flatten_results = [item for sublist in results for item in sublist]
for rating in flatten_results:
    print(f"[{rating.stars}] {rating.name} [{rating.date_rated}] {rating.info} [{rating.url}]")

print(f"Time taken: {end:.24}s")
print(f'len(results): {len(flatten_results)}')
