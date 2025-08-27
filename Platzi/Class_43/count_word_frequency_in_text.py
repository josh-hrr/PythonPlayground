# Counting word frequencies in a text

from collections import defaultdict

def count_words_in_text(text: list[str]) -> defaultdict:
  new_dictionary = defaultdict(int)
  for word in text:
    new_dictionary[word] += 1
  return new_dictionary

large_text = "hello world this is a test hello"
large_test_list = large_text.split()
print(count_words_in_text(large_test_list))