'''

pip: is the equivalent of npm for Javascript.
It is a package manager for Python packages.

pip freeze: list of all packages installed in the global environment.


'''

import matplotlib.pyplot as plt

def generate_pie_chart():
  labels = ['Python', 'Javascript', 'Typescript']
  values = [50, 30, 20]
  colors = ['#008fd5', "#f4ff61", "#2d5efd"] 
  plt.pie(values, labels=labels, colors=colors, shadow=True, startangle=50)
  plt.axis('equal')
  plt.title('Programming languages')
  plt.savefig('pie_chart.png')
  plt.show()

generate_pie_chart()

