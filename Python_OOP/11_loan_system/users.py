from exceptions import InvalidTitleError

class User:
  def __init__(self, name: str, DPI: str):
    self.name = name
    self.DPI = DPI 
    self.career: str | None
    # initialize the borrowed books list so subclasses can use it
    self.books_borrowed: list[str] = []
 
  def request_book(self, title: str):
    return f"The request of the book {title} has been submitted! " 
  
  def return_book(self, title: str):
    return f"The return of the book {title} has been submitted! "
  
  def get_books_requested(self):
    return f"The books requested look as follows: {self.books_borrowed}"
   
  def get_poly_example(self) -> str:
    return "Poly example" 
  
class Profesor(User):
  def __init__(self, name: str, DPI: str):
    super().__init__(name, DPI)
    self.book_limit = None
 
  def request_book(self, title:str) -> str:
    self.books_borrowed.append(title)
    return f"The book {title} has been authorized!" 
   
  def get_poly_example(self) -> str: 
    return "Poly example from professor!" 
  
class Student(User):
  def __init__(self, name: str, DPI: str, career: str):
    super().__init__(name, DPI)
    self.career = career
    self.book_limit = 3
  
  def request_book(self, title: str):
    if not title:
      raise InvalidTitleError(f"request_book error, the book does not exist. {title}.") #raise stops execution

    if len(self.books_borrowed) < self.book_limit:
      self.books_borrowed.append(title)
      return f"Book {title} has been authorized!"
    else:
      return "Cannot borrowed more books, limit has been reached!"
    
  def return_book(self, title: str): 
    if not title:
      raise InvalidTitleError(f"return_book error, the book does not exist. {title}.") 
    if len(self.books_borrowed) != 0:
      self.books_borrowed.remove(title)
      return f"Book {title} has been returned!"
    else: 
      return "Cannot returned the specified book" 
    
         

    

