
'''

module: functions, variables or clases to reuse in other files

reusability and organization of code
genreates a pycache file __pycache__
maintanability 

'''

# generate sales reports for a specific month
def generate_sales_report(month, sales):
  return f'Sales Report - {month}: Total Sales: ${sales}'

def generate_expenses_report(month, expenses):
  return f'Expenses Report - {month}: Total Expenses: ${expenses}'

