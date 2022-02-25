import time
import threading
import queue
from datetime import datetime


# vytvoření fronty
q = queue.Queue()


# simulace producenta
def producer():
    name = threading.current_thread().name
    for job in range(5):
        print(f'{name} thread: Starting producing {job} [{datetime.utcnow().strftime("%H:%M:%S.%f")[:-3]}]')
        q.put(job)
        time.sleep(0.3)
        print(f'{name} thread: Produced {job} [{datetime.utcnow().strftime("%H:%M:%S.%f")[:-3]}]')


# simulace konzumenta
def consumer():
    name = threading.current_thread().name
    while True:
        job = q.get()
        print(f'{name} thread: Starting consuming {job} [{datetime.utcnow().strftime("%H:%M:%S.%f")[:-3]}]')
        time.sleep(0.4)
        print(f'{name} thread: Consumed {job} [{datetime.utcnow().strftime("%H:%M:%S.%f")[:-3]}]')
        q.task_done()


# spuštění konzumentů
threading.Thread(target=consumer, daemon=True, name="1st").start()
threading.Thread(target=consumer, daemon=True, name="2nd").start()
# threading.Thread(target=consumer, daemon=True, name="3rd").start()

# spuštění producentů
threading.Thread(target=producer, daemon=True, name="1st").start()
threading.Thread(target=producer, daemon=True, name="2nd").start()
threading.Thread(target=producer, daemon=True, name="3rd").start()
# threading.Thread(target=producer, daemon=True, name="3rd").start()

# čekání na zpracování všech zpráv ve frontě
q.join()
print('Done')


# 1st thread: Starting producing 0 [14:06:48.435]
# 2nd thread: Starting consuming 0 [14:06:48.436]
# 2nd thread: Starting producing 0 [14:06:48.438]
# 1st thread: Starting consuming 0 [14:06:48.439]
# 3rd thread: Starting producing 0 [14:06:48.439]
# 1st thread: Produced 0 [14:06:48.736]
# 1st thread: Starting producing 1 [14:06:48.736]
# 2nd thread: Produced 0 [14:06:48.739]
# 2nd thread: Starting producing 1 [14:06:48.739]
# 3rd thread: Produced 0 [14:06:48.740]
# 3rd thread: Starting producing 1 [14:06:48.740]
# 2nd thread: Consumed 0 [14:06:48.837]
# 2nd thread: Starting consuming 0 [14:06:48.837]
# 1st thread: Consumed 0 [14:06:48.840]
# 1st thread: Starting consuming 1 [14:06:48.840]
# 1st thread: Produced 1 [14:06:49.037]
# 1st thread: Starting producing 2 [14:06:49.037]
# 2nd thread: Produced 1 [14:06:49.039]
# 2nd thread: Starting producing 2 [14:06:49.039]
# 3rd thread: Produced 1 [14:06:49.040]
# 3rd thread: Starting producing 2 [14:06:49.040]
# 2nd thread: Consumed 0 [14:06:49.238]
# 2nd thread: Starting consuming 1 [14:06:49.238]
# 1st thread: Consumed 1 [14:06:49.240]
# 1st thread: Starting consuming 1 [14:06:49.240]
# 1st thread: Produced 2 [14:06:49.337]
# 1st thread: Starting producing 3 [14:06:49.338]
# 2nd thread: Produced 2 [14:06:49.340]
# 2nd thread: Starting producing 3 [14:06:49.340]
# 3rd thread: Produced 2 [14:06:49.341]
# 3rd thread: Starting producing 3 [14:06:49.341]
# 1st thread: Produced 3 [14:06:49.638]
# 1st thread: Starting producing 4 [14:06:49.638]
# 2nd thread: Consumed 1 [14:06:49.638]
# 2nd thread: Starting consuming 2 [14:06:49.638]
# 2nd thread: Produced 3 [14:06:49.640]
# 2nd thread: Starting producing 4 [14:06:49.640]
# 1st thread: Consumed 1 [14:06:49.641]
# 1st thread: Starting consuming 2 [14:06:49.641]
# 3rd thread: Produced 3 [14:06:49.641]
# 3rd thread: Starting producing 4 [14:06:49.641]
# 1st thread: Produced 4 [14:06:49.938]
# 2nd thread: Produced 4 [14:06:49.941]
# 3rd thread: Produced 4 [14:06:49.942]
# 2nd thread: Consumed 2 [14:06:50.039]
# 2nd thread: Starting consuming 2 [14:06:50.039]
# 1st thread: Consumed 2 [14:06:50.041]
# 1st thread: Starting consuming 3 [14:06:50.041]
# 2nd thread: Consumed 2 [14:06:50.440]
# 2nd thread: Starting consuming 3 [14:06:50.440]
# 1st thread: Consumed 3 [14:06:50.442]
# 1st thread: Starting consuming 3 [14:06:50.442]
# 2nd thread: Consumed 3 [14:06:50.840]
# 2nd thread: Starting consuming 4 [14:06:50.841]
# 1st thread: Consumed 3 [14:06:50.843]
# 1st thread: Starting consuming 4 [14:06:50.843]
# 2nd thread: Consumed 4 [14:06:51.241]
# 2nd thread: Starting consuming 4 [14:06:51.241]
# 1st thread: Consumed 4 [14:06:51.243]
# 2nd thread: Consumed 4 [14:06:51.642]
# Done