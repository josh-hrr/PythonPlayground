import matplotlib.pyplot as pyplot
import csv

'''

Figure object: "fig", the whole window/canvas.
Axes object: "ax", area inside the figure object, schema.

read csv
extract: population year: population number
iterate over the dictionary, pass the values into the ax.bar(year, number)


'''

def generate_bar_chart(labels, values, country='default'):
  fig, ax = pyplot.subplots()
  ax.bar(labels, values) 
  pyplot.savefig(f'{country}.png') 

def generate_pie_chart(labels, values):
  fig, ax = pyplot.subplots()
  wedges, texts = ax.pie(values) 

  ax.legend(
    wedges,
    labels,
    title="Countries",
    loc="center left",
    bbox_to_anchor=(1,0,0.5,1)
  )

  ax.axis("equal")
  
  pyplot.savefig('generate_pie_chart.png') 

  
def read_csv(path):
  with open(path, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)   
    my_data = []
    for row in reader:
      my_dict = zip(header, row)  
      my_data.append(dict(my_dict))
    return my_data
  
def get_all_world_population_percentage(my_data):
  my_new_dictionary = {}
  for value in my_data:  
      my_new_dictionary[value['Country/Territory']] = value['World Population Percentage'] 
  my_labels = list(my_new_dictionary.keys())
  my_values = list(my_new_dictionary.values())
  return my_labels, my_values

def get_all_population_by_year(my_data): 
  my_population_by_year = []
  my_population_by_year_2022 = []
  my_population_by_year_2020 = []
  my_population_by_year_2015 = []  
  for key in my_data: 
    if key['2022 Population']: 
      my_population_by_year_2022.append(int(key['2022 Population']))
    if key['2020 Population']: 
      my_population_by_year_2020.append(int(key['2020 Population']))
    if key['2015 Population']: 
      my_population_by_year_2015.append(int(key['2015 Population'])) 
  my_population_by_year.append({
    '2022': sum(my_population_by_year_2022),
    '2020': sum(my_population_by_year_2020),
    '2015': sum(my_population_by_year_2015)
  })
  return my_population_by_year

def get_data_by_country(my_data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, my_data))
  return result

def get_population_country(country_dict):
  my_dictionary = {
    '1970': int(country_dict[0]['1970 Population']),
    '1980': int(country_dict[0]['1980 Population']),
  }  
  labels = list(my_dictionary.keys())
  values = list(my_dictionary.values())
  return labels, values 

if __name__ == '__main__': 
  labels = ['a', 'b', 'c']
  values = [100, 200, 80] 
  generate_bar_chart(labels, values) 
  my_file = read_csv('data.csv')
   
  my_population_by_year = get_all_population_by_year(my_file) 
  for year_data in my_population_by_year:
    my_labels = list(year_data.keys())
    my_values = list(year_data.values())
    generate_bar_chart(my_labels, my_values)

  country_name = input("Enter country name: ")


  data_by_country = get_data_by_country(my_file, country_name)
  c_label, c_population = get_population_country(data_by_country)
  generate_bar_chart(c_label, c_population, country_name)

  print("****get_all_world_population_percentage****")
  p_label, p_values = get_all_world_population_percentage(my_file)
  generate_pie_chart(p_label, p_values)

