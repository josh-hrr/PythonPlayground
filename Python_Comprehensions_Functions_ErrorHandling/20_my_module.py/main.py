from utils import get_population_by_country

data = [
  {
    "Country": "GT",
    "Population": 100
  },
  {
    "Country": "USA",
    "Population": 500
  }
]
result = get_population_by_country(data, 'GT')
print(result)