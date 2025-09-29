with open('text.txt', 'w', encoding='utf-8') as file:
  file.write('starting point overrides existing content if file exists○')
  file.write('\nif file does not exists, it is created 🍟')