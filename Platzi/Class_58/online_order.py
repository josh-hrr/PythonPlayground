import asyncio
import time
import random
import multiprocessing

#' Async' function to verify stock
async def verify_stock(item):
  print(f'Verifying stock for {item}...')
  await asyncio.sleep(random.randint(1,5)) # Simulate network delay
  print(f'Stock verified for {item}.')
  return random.choice([True, False])

# 'Async' function to process payment
async def process_payment(amount):
  print(f'Processing payment of ${amount}...')
  await asyncio.sleep(random.randint(1,5)) # Simulate network delay
  print(f'Payment of ${amount} processed.')
  return True

# 'Async' function to to calculating total order cost 
def calculate_total(order):
  print(f'Calculating total order cost for {len(order)} items...')
  asyncio.sleep(5) 
  total = sum(item['price'] * item['quantity'] for item in order)
  print(f'Total order cost calculated: ${total}.')
  return total

async def process_order(order_id, items):
  print(f'Starting processing order {order_id}...')

  # Step 1: Verify stock for each item
  stock_tasks = [verify_stock(item['name']) for item in items]
  stock_results = await asyncio.gather(*stock_tasks)

  if not all(stock_results):
    print(f'Order {order_id} cannot be processed due to insufficient stock.')
    return

  # Step 2: Calculate total cost using multiprocessing
  with multiprocessing.Pool() as pool:
    total_cost = pool.apply(calculate_total, (items,))

  # Step 3: Process payment
  payment_success = await process_payment(order_id)
  
  if payment_success:
    print(f'Order {order_id} processed successfully with total cost ${total_cost}.')
  else:
    print(f'Order {order_id} failed during payment processing.')

async def main():
  orders = [
    {
      'order_id': 1, 
      'items': [
        {
          'name': 'item1', 
          'price': 10, 
          'quantity': 2
        }, 
        {
          'name': 'item2', 
          'price': 15, 
          'quantity': 1
        }]
    },
    {
      'order_id': 2, 
      'items': [
        {
          'name': 'item3', 
          'price': 20, 
          'quantity': 1
        }, 
        {
          'name': 'item4', 
          'price': 25, 
          'quantity': 3
        }]
      },
    {'order_id': 3, 
      'items': [
        {
          'name': 'item5', 
          'price': 30, 
          'quantity': 2
        }, 
        {
          'name': 'item6', 
          'price': 35, 
          'quantity': 1
        }]
    }
  ]

  order_tasks = [process_order(order['order_id'], order['items']) for order in orders]
  await asyncio.gather(*order_tasks)

if __name__ == '__main__':
  asyncio.run(main()) 