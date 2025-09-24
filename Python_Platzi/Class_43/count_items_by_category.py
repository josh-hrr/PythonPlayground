from collections import defaultdict

products = [
    ("Fruit", "apple"),
    ("Fruit", "banana"),
    ("Vegetable", "carrot"),
    ("Vegetable", "spinach")
]

def count_items_by_category(products: list[tuple]) -> defaultdict:
  products_categorized = defaultdict(list)
  for category, product in products:
    products_categorized[category].append(product)
  return products_categorized

print(count_items_by_category(products))