import asyncio
import random

async def download_process(file):
  print(f'Downloading file {file}')
  time = random.randint(1,10)
  await asyncio.sleep(time)
  print(f'{file} downloaded.')
  return file

async def main():
  print('Starting download...')
  result1 = await download_process('file1')
  result2 = await download_process('file2')
  result3 = await download_process('file3')
  print(f'{result1, result2, result3}')

asyncio.run(main())