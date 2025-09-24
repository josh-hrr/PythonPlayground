import reports 

'''

module: 
1. functions, variables or clases to reuse in other files
genreates a pycache file __pycache__

pycache: 
1. compiles the source files into bytecode 
2. this makes the program run faster when used again
3. it is specific to the python version in use
4. improves performance 


'''
# Genreate report of sales and expenses using 'reports' module

sales_report = reports.generate_sales_report('October', 10000)
expenses_report = reports.generate_expenses_report('October', 5000)

print(sales_report)
print(expenses_report)