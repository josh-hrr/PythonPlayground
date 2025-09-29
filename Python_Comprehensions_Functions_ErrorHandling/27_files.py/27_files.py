file = open('text.txt')

#file.read()      reads the whole text file, heavy in memory usage.
#print(file.readline())   reads each line

for line in file:
  print(line)
file.close()


#it closes the file automatically:
with open('text1.txt') as file:
  for line in file:
    print(line)