from Usuario import Usuario

class Estudiante(Usuario):
  def __init__(self, name, DPI, career):
    super().__init__(name, DPI)
    self.career = career
    self.book_limit = 3
  
  def request_book(self, title):
    if len(self.books_borrowed) < self.book_limit:
      self.books_borrowed.append(title)
      return f"Book {title} has been authorized!"
    else:
      return f"Cannot borrowed more books, limit has been reached!"
    
