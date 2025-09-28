'''

import excercise:

creates a new module "my_functions.py"
it gets imported in "main.py"
list comprehension to create a list of every total occurance from the list-dictionary
sum function: sums all items in a list
'''

from my_functions import get_totals_list, get_sum_totals

orders = [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]

list_totals = get_totals_list(orders)
sum_totals_list = get_sum_totals(list_totals)
print(sum_totals_list)