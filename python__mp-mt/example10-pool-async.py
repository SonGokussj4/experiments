from multiprocessing import Pool
from datetime import datetime
from os import getuid
import time
from .example10_functions import get_url
from pprint import pprint

pool = Pool(processes=6)

# results = []

# def get_url(url):
#     print(f'')
#     print(f'Getting {url} [{datetime.utcnow().strftime("%H:%M:%S.%f")[:-3]}]')
#     time.sleep(0.5)
#     results.append(url)
#     return url

class Results():
    def __init__(self):
        self.vals = []

    def update_result(self, val):
        self.vals.append(val)

classResults = Results()

for i in range(50):
#   res = pool.apply_async(get_url, ('https://seznam.cz',))
  pool.apply_async(get_url, ('https://seznam.cz',), callback=classResults.update_result)
#   results.append(res)

while pool._cache:
  print("number of jobs pending: ", len(pool._cache))
  time.sleep(1)

pool.close()
pool.join()

print("ClassResults")
pprint(classResults.vals)


print("ListComprehentionResults")
# results = [res.get() for res in results]
# pprint(results)

print('done')
