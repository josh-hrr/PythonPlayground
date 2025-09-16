'''
Unlike threads, processes do not share memory by default. To allow two processes to share data, Python provides tools such as `multiprocessing.Queue` and `multiprocessing.Value`.

'''

import multiprocessing

def calculate_square(numbers, queue):
  for n in numbers:
      queue.put(n * n)

if __name__ == "__main__":
  numbers = [1, 2, 3, 3, 4, 5]
  queue = multiprocessing.Queue()

  process = multiprocessing.Process(target=calculate_square, args=(numbers, queue))
  process.start()
  process.join()

  # Extract results from the queue
  while not queue.empty():
      print(queue.get())