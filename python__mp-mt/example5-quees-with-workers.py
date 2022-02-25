import time
import threading
import queue
from datetime import datetime


# vytvoření fronty
q = queue.Queue()


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
threading.Thread(target=consumer, daemon=True, name="3rd").start()

# vytvoření úloh v producentovi
for job in range(10):
    print(f'Producing {job}')
    q.put(job)

# čekání na zpracování všech zpráv ve frontě
q.join()
print('Done')


# (jverner@tacticus) - (~/GIT/EXPERIMENTS/threading-root-cz) $ python3.9eve example5-quees-with-workers.py
# Producing 0
# Producing 1
# 1st thread: Starting consuming 0 [08:55:09.410]
# Producing 2
# 2nd thread: Starting consuming 1 [08:55:09.410]
# Producing 3
# 3rd thread: Starting consuming 2 [08:55:09.410]
# Producing 4
# Producing 5
# Producing 6
# Producing 7
# Producing 8
# Producing 9
# 1st thread: Consumed 0 [08:55:09.811]
# 2nd thread: Consumed 1 [08:55:09.811]
# 1st thread: Starting consuming 3 [08:55:09.811]
# 2nd thread: Starting consuming 4 [08:55:09.811]
# 3rd thread: Consumed 2 [08:55:09.811]
# 3rd thread: Starting consuming 5 [08:55:09.811]
# 1st thread: Consumed 3 [08:55:10.212]
# 2nd thread: Consumed 4 [08:55:10.212]
# 1st thread: Starting consuming 6 [08:55:10.212]
# 2nd thread: Starting consuming 7 [08:55:10.212]
# 3rd thread: Consumed 5 [08:55:10.212]
# 3rd thread: Starting consuming 8 [08:55:10.212]
# 1st thread: Consumed 6 [08:55:10.613]
# 2nd thread: Consumed 7 [08:55:10.613]
# 3rd thread: Consumed 8 [08:55:10.613]
# 1st thread: Starting consuming 9 [08:55:10.613]
# 1st thread: Consumed 9 [08:55:11.014]
# Done
