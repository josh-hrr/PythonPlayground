import csv, functools

def read_csv(path):
   # Solution 👇
   with open(path, 'r') as my_file:
      reader = csv.reader(my_file, delimiter=',') 
      data = []
      total = 'total'
      counter = 0
      for row in reader:   
         counter = counter + 1 
         key, value = row
         data.append({
            key: counter,
            total: value
         })   
      
      only_totals = [int(value['total']) for value in data]

      #solution 1 - reduce
      my_sum = functools.reduce(lambda x, y: x + y, only_totals)
      return my_sum

      #solution 2 - counter
      my_sum = 0
      for value in data:
         my_sum = my_sum + int(value['total'])
      return my_sum

      #solution 3 - sum
      return sum(only_totals)
      
if __name__ == '__main__': 
  response = read_csv('data.csv')
  print('the total of expenses is: ', response)