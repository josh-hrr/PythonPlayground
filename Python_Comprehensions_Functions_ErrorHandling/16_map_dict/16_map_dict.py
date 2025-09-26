items = [
  {
    'product': 'shirt',
    'price': 100
  },
  {
    'product': 'pants',
    'price': 150
  },
  {
    'product': 'jacket',
    'price': 200
  }
]

prices = list(map(lambda item: item['price'], items))
print(prices) # [100, 150, 200]

#rewrites original items dict
def add_taxes(item):
  item['taxes'] = item['price'] * .19 #we need to use copy to reference the dict to a new memory space
  return item

new_items = list(map(add_taxes, items))
print(new_items)

