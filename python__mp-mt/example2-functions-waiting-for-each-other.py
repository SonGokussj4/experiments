import threading
import time


def worker(threadName, delay, n):
    threadName = threading.current_thread().name
    print(threadName, 'Starting')
    for counter in range(1, n+1):
        time.sleep(delay)
        print("{}: {}/{} - {}".format(threadName, counter, n, time.ctime(time.time())))
        numbers.append("{}: {}/{}".format(threadName, counter, n))
    print(threadName, 'Done')

numbers = []
print("main started")

t1 = threading.Thread(target=worker, args=("Thread-1", 0.1, 20))
t2 = threading.Thread(target=worker, args=("Thread-2", 1.0, 3))

t1.start()
t2.start()

t1.join()
t2.join()

from pprint import pprint
pprint(numbers)

print("main finished")


# (jverner@tacticus) - (~/GIT/EXPERIMENTS/threading-root-cz) $ python3.9eve example2-functions-waiting-for-each-other.py
# main started
# Thread-1 Starting
# Thread-2 Starting
# Thread-1: 1/20 - Tue Feb 22 09:34:36 2022
# Thread-1: 2/20 - Tue Feb 22 09:34:36 2022
# Thread-1: 3/20 - Tue Feb 22 09:34:36 2022
# Thread-1: 4/20 - Tue Feb 22 09:34:36 2022
# Thread-1: 5/20 - Tue Feb 22 09:34:37 2022
# Thread-1: 6/20 - Tue Feb 22 09:34:37 2022
# Thread-1: 7/20 - Tue Feb 22 09:34:37 2022
# Thread-1: 8/20 - Tue Feb 22 09:34:37 2022
# Thread-1: 9/20 - Tue Feb 22 09:34:37 2022
# Thread-2: 1/3 - Tue Feb 22 09:34:37 2022
# Thread-1: 10/20 - Tue Feb 22 09:34:37 2022
# Thread-1: 11/20 - Tue Feb 22 09:34:37 2022
# Thread-1: 12/20 - Tue Feb 22 09:34:37 2022
# Thread-1: 13/20 - Tue Feb 22 09:34:37 2022
# Thread-1: 14/20 - Tue Feb 22 09:34:37 2022
# Thread-1: 15/20 - Tue Feb 22 09:34:38 2022
# Thread-1: 16/20 - Tue Feb 22 09:34:38 2022
# Thread-1: 17/20 - Tue Feb 22 09:34:38 2022
# Thread-1: 18/20 - Tue Feb 22 09:34:38 2022
# Thread-1: 19/20 - Tue Feb 22 09:34:38 2022
# Thread-2: 2/3 - Tue Feb 22 09:34:38 2022
# Thread-1: 20/20 - Tue Feb 22 09:34:38 2022
# Thread-1 Done
# Thread-2: 3/3 - Tue Feb 22 09:34:39 2022
# Thread-2 Done
# ['Thread-1: 1/20',
#  'Thread-1: 2/20',
#  'Thread-1: 3/20',
#  'Thread-1: 4/20',
#  'Thread-1: 5/20',
#  'Thread-1: 6/20',
#  'Thread-1: 7/20',
#  'Thread-1: 8/20',
#  'Thread-1: 9/20',
#  'Thread-2: 1/3',
#  'Thread-1: 10/20',
#  'Thread-1: 11/20',
#  'Thread-1: 12/20',
#  'Thread-1: 13/20',
#  'Thread-1: 14/20',
#  'Thread-1: 15/20',
#  'Thread-1: 16/20',
#  'Thread-1: 17/20',
#  'Thread-1: 18/20',
#  'Thread-1: 19/20',
#  'Thread-2: 2/3',
#  'Thread-1: 20/20',
#  'Thread-2: 3/3']
# main finished