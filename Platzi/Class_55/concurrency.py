'''
concurrency:


definition: manages multiple threads progressively 
ideal usage: I/O operations, network waits, files writing
implementaion: threading, asyncio


'''

import threading
import time

def process_request(request_id):
  print(f'Procesando solicitud {request_id}')
  time.sleep(3)
  print(f'Solicitud {request_id} completada')

threads = []

for i in range(3):
  thread = threading.Thread(target=process_request, args=(i,))
  threads.append(thread)
  thread.start()

for thread in threads:
  thread.join() #ensures it waits until each thread completes

print('Todas las solicitudes completadas')