from Usuario import Usuario
from Exceptions import InvalidTitleError

class Estudiante(Usuario):
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
    
    for book in self.books_borrowed:
      if book == title:
        if len(self.books_borrowed) != 0:
          self.books_borrowed.remove(title)
          return f"Book {title} has been returned!"
        else: 
          return "Cannot returned the specified book"
      else:
        return "Book does not exist!"
    return ""
         

    



    
