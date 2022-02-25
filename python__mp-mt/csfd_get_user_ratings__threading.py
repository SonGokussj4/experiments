from pprint import pprint
import concurrent.futures
import requests
from bs4 import BeautifulSoup as bs
import time
from multiprocessing import Pool, cpu_count

from csfd_functions import get_csfd_ratings_from_url, get_csfd_max_page


BASE_URL = "https://www.csfd.cz"
UZIVATEL_URL = BASE_URL + "/uzivatel/"

CONNECTIONS = 2
TIMEOUT = 5

# CPU_COUNT = cpu_count()
# pool = Pool(processes=CPU_COUNT)


class Results():
    def __init__(self):
        self.vals = []

    def update_result(self, val):
        self.vals.append(val)

# results = Results()
results = []

# user_id = "78145-songokussj"
user_id = "78145"
max_page = get_csfd_max_page(user_id)
urls = [UZIVATEL_URL + user_id + f"/hodnoceni/?page={page_num}" for page_num in range(1, max_page + 1)]

start = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
    future_to_url = (executor.submit(get_csfd_ratings_from_url, url,) for url in urls)
    for future in concurrent.futures.as_completed(future_to_url):
        try:
            data = future.result()
        except Exception as exc:
            data = str(type(exc))
        finally:
            results.append(data)

# for page_num in range(1, max_page + 1):
# #   res = pool.apply_async(get_url, ('https://seznam.cz',))
#   pool.apply_async(get_csfd_ratings, (user_id, page_num), callback=results.update_result)
# #   results.append(res)

# while pool._cache:
#   print("number of jobs pending: ", len(pool._cache))
#   time.sleep(0.1)

# pool.close()
# pool.join()

end = start - time.time()

flatten_results = [item for sublist in results for item in sublist]
for rating in flatten_results:
    print(f"[{rating.stars}] {rating.name} [{rating.date_rated}] {rating.info} [{rating.url}]")

print(f"Time taken: {end:.24}s")
print(f'len(results): {len(flatten_results)}')
