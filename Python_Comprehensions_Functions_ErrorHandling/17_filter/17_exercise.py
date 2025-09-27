'''

filter by the words that len is >= 4

'''

def filter_by_length(words):
   # Escribe tu solución 👇
   result = filter(lambda item: len(item) >= 4, words)
   return list(result)

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)