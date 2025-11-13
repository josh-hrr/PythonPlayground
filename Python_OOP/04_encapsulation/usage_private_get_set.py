'''

isPopular if book has been borrowed for more than 5 times.
to declare a private, we just use "__" before the var name.
'''
class Book:  
  def __init__(self, name, description, available):
    self.name = name
    self.description = description
    self.available = available 
    self.__set_borrow_counter = 0
  
  def __str__(self):
    return f'Printing details: {self.name}, {self.description}, {self.available}' 

  def set_availability(self, new_availability):
    if self.available == True:
      self.available = new_availability
    else:
      return f"The book '{self.name}' has been borrowed!"
    
  def set_borrow(self):
    if self.available == True:
      self.available = False
      self.__set_borrow_counter = self.__set_borrow_counter + 1
  
  def set_return(self):
    if self.available == False:
      self.available = True
  
  def is_popular(self):
    result = self.__set_borrow_counter > 2 
    return result
  
  def get_times_borrowed(self):
    print(self.__set_borrow_counter)
    return self.__set_borrow_counter
  
  def set_times_borrowed(self, times_borrowed):
    self.__set_borrow_counter = times_borrowed


if __name__ == '__main__':
  book1 = Book("book1", "bookDesc1", False)
  book2 = Book("book2", "bookDesc2", True)  
  list = [book1, book2]
  book2.set_borrow()
  book2.set_return()

  book2.set_borrow()
  book2.set_return()

  book2.set_borrow()
  book2.set_return() 

  is_popular_result = book2.is_popular()
  print("Printing is_popular", is_popular_result)

  book2.get_times_borrowed()
  book2.set_times_borrowed(50)
  book2.get_times_borrowed()

  for book in list:
    print(book)

    
  