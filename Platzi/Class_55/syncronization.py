'''
definition: allow only one thread to access a resource at a time
ideal usage: when multiple threads access shared data, example: withdrawing a bank account balance
implementation: threading.Lock

'''
import threading

# Simulating a bank account with a balance
balance = 0
lock = threading.Lock() # Create a lock object

def deposit(money):
  global balance # why global? because we are modifying the global variable
  for _ in range(100000): # why _? because we don't care about the variable, why 100000? to simulate a long process.
    with lock:
      balance = balance + money

threads = []
for _ in range(2):
  thread = threading.Thread(target=deposit, args=(1,))
  threads.append(thread)
  thread.start()
 
for thread in threads: 
  print("Thread: ", thread.name)
  thread.join()

print(f'Ending balance: {balance}') # Expected: 200000

