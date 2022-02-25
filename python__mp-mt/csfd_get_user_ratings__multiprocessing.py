from pprint import pprint
import requests
from bs4 import BeautifulSoup as bs
import time
from multiprocessing import Pool, cpu_count

from csfd_functions import get_csfd_ratings, get_csfd_max_page


BASE_URL = "https://www.csfd.cz"
UZIVATEL_URL = BASE_URL + "/uzivatel/"
CPU_COUNT = cpu_count()
pool = Pool(processes=2)


class Rating:
    def __init__(self, name):
        self.name = name
        self.stars = ""
        self.url = ""
        self.date_rated = ""
        self.info = ""


class Results():
    def __init__(self):
        self.vals = []

    def update_result(self, val):
        self.vals.append(val)

results = Results()


# user_id = "78145-songokussj"
user_id = "78145"
max_page = get_csfd_max_page(user_id)

start = time.time()

for page_num in range(1, max_page + 1):
#   res = pool.apply_async(get_url, ('https://seznam.cz',))
  pool.apply_async(get_csfd_ratings, (user_id, page_num), callback=results.update_result)
#   results.append(res)

while pool._cache:
  print("number of jobs pending: ", len(pool._cache))
  time.sleep(0.1)

pool.close()
pool.join()

end = round(start - time.time(), 4)

flatten_results = [item for sublist in results.vals for item in sublist]
for rating in flatten_results:
    print(f"[{rating.stars}] {rating.name} [{rating.date_rated}] {rating.info} [{rating.url}]")

print(f"Time taken: {end}s")
print(f'len(flatten_results): {len(flatten_results)}')
