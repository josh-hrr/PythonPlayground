'''
definition: allow only one thread to access a resource at a time
ideal usage: when multiple threads access shared data, example: withdrawing a bank account balance
implementation: threading.Lock

'''
#example 1 - no Lock
import threading, time, sys

lock = threading.Lock()
globalBalance = 0
def deposit(money): 
    global globalBalance
    for _ in range(2000):
        with lock:                        # if you comment this line, you will see a wrong balance at the end
          readBalance = globalBalance     # read
          time.sleep(0)                   # let another thread to run if one is waiting
          readBalance = readBalance + money
          globalBalance = readBalance     # write

threads = [] 

for _ in range(2):
    thread = threading.Thread(target=deposit, args=(1,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join() #ensures it waits until each thread completes

print("Ending balance:", globalBalance, " (expected:", 2*2000, ")")  