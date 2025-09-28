try:
  print(1/0)
  assert 1 != 1, '1 is not equal to 1'
except Exception as error:
   print("Error:", error)
except ZeroDivisionError as zeroError:
  print("Error:", zeroError)


print("this will continue to execute...")