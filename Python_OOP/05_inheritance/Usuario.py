class Usuario:
  def __init__(self, name, DPI):
    self.name = name
    self.DPI = DPI 
    self.books_borrowed = []

  def request_book(self, title):
    return f"The request of the book {title} has been submitted! "
  
  def return_book(self, title):
    return f"The return of the book {title} has been submitted! "
  
  def get_books_requested(self):
    return f"The books requested look as follows: {self.books_borrowed}"
