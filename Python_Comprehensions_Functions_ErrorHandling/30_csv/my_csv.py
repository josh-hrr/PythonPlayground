import csv
 
def read_csv(path):
  with open(path, 'r') as file:
    reader = csv.reader(file, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row) 
      country_dictionary = {key: value for key, value in iterable} 
      data.append(country_dictionary)
    return data 

if __name__ == '__main__':
  my_data = read_csv('data.csv')
  print(my_data[0])