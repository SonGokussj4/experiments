# https://www.root.cz/clanky/soubezne-a-paralelne-bezici-ulohy-naprogramovane-v-pythonu

import threading
import time


def worker(threadName, delay, n):
    threadName = threading.current_thread().name
    print(threadName, 'Starting')
    for counter in range(1, n+1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(threadName, counter, n, time.ctime(time.time())))
    print(threadName, 'Done')


threading.Thread(target=worker, args=("Thread-1", 0.1, 20)).start()
threading.Thread(target=worker, args=("Thread-2", 1.0, 3)).start()


# (jverner@tacticus) - (~/GIT/EXPERIMENTS/threading-root-cz) $ python3.9eve main.py
# Thread-1 Starting
# Thread-2 Starting
# Thread-1: 1/50 - Tue Feb 22 09:19:37 2022
# Thread-1: 2/50 - Tue Feb 22 09:19:37 2022
# Thread-1: 3/50 - Tue Feb 22 09:19:37 2022
# Thread-1: 4/50 - Tue Feb 22 09:19:37 2022
# Thread-1: 5/50 - Tue Feb 22 09:19:38 2022
# Thread-1: 6/50 - Tue Feb 22 09:19:38 2022
# Thread-1: 7/50 - Tue Feb 22 09:19:38 2022
# Thread-1: 8/50 - Tue Feb 22 09:19:38 2022
# Thread-1: 9/50 - Tue Feb 22 09:19:38 2022
# Thread-2: 1/5 - Tue Feb 22 09:19:38 2022
# Thread-1: 10/50 - Tue Feb 22 09:19:38 2022
# Thread-1: 11/50 - Tue Feb 22 09:19:38 2022
# Thread-1: 12/50 - Tue Feb 22 09:19:38 2022
# Thread-1: 13/50 - Tue Feb 22 09:19:38 2022
# Thread-1: 14/50 - Tue Feb 22 09:19:38 2022
# Thread-1: 15/50 - Tue Feb 22 09:19:39 2022
# Thread-1: 16/50 - Tue Feb 22 09:19:39 2022
# Thread-1: 17/50 - Tue Feb 22 09:19:39 2022
# Thread-1: 18/50 - Tue Feb 22 09:19:39 2022
# Thread-1: 19/50 - Tue Feb 22 09:19:39 2022
# Thread-2: 2/5 - Tue Feb 22 09:19:39 2022
