'''

paralelism:

definition: executes simultaniously every task
ideal usage: tasks require much calculation
implementation: 

'''

import multiprocessing

def calculate_square(n):
  return n*n

if __name__ == '__main__':
  numbers = [1, 2, 3, 4, 5]

  with multiprocessing.Pool() as pool:
    results = pool.map(calculate_square, numbers)
  print(f'Resultados: {results}')