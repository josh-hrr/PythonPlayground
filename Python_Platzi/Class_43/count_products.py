from collections import defaultdict #defaults a value in case does not exists in the dictionary

def count_products(orders: list[str]) -> defaultdict:
  product_count = defaultdict(str)
  print(type(product_count))
  for product in orders:
    product_count[product] += "test"
  return product_count

orders = ['laptop', 'smartphone', 'laptop', 'table']
count = count_products(orders)
print(count)


