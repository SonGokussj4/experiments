import threading
import time
import queue
from datetime import datetime

# vytvoření fronty
q = queue.Queue()


# simulace konzumenta
def consumer():
    while True:
        job = q.get()
        print(f'Starting consuming {job} [{datetime.utcnow().strftime("%H:%M:%S.%f")[:-3]}]')
        time.sleep(0.4)
        print(f'Consumed {job} [{datetime.utcnow().strftime("%H:%M:%S.%f")[:-3]}]')
        q.task_done()


# spuštění konzumenta
threading.Thread(target=consumer, daemon=True, name="první").start()

# vytvoření úloh v producentovi
for job in range(10):
    print(f'Producing {job}')
    q.put(job)

# čekání na zpracování všech zpráv ve frontě
q.join()
print('Done')

# from pprint import pprint
# pprint(numbers)

# (jverner@tacticus) - (~/GIT/EXPERIMENTS/threading-root-cz) $ python3.9eve example4-quees.py
# Producing 0
# Producing 1
# Starting consuming 0 [08:52:38.770]
# Producing 2
# Producing 3
# Producing 4
# Producing 5
# Producing 6
# Producing 7
# Producing 8
# Producing 9
# Consumed 0 [08:52:39.171]
# Starting consuming 1 [08:52:39.171]
# Consumed 1 [08:52:39.572]
# Starting consuming 2 [08:52:39.572]
# Consumed 2 [08:52:39.972]
# Starting consuming 3 [08:52:39.972]
# Consumed 3 [08:52:40.373]
# Starting consuming 4 [08:52:40.373]
# Consumed 4 [08:52:40.774]
# Starting consuming 5 [08:52:40.774]
# Consumed 5 [08:52:41.174]
# Starting consuming 6 [08:52:41.175]
# Consumed 6 [08:52:41.575]
# Starting consuming 7 [08:52:41.575]
# Consumed 7 [08:52:41.976]
# Starting consuming 8 [08:52:41.976]
# Consumed 8 [08:52:42.376]
# Starting consuming 9 [08:52:42.377]
# Consumed 9 [08:52:42.777]
# Done
