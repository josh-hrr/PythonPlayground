class Usuario:
  def __init__(self, name, DPI):
    self.name = name
    self.DPI = DPI 
    self.books_borrowed = []

  def request_book(self, title):
    return f"The request of the book {title} has been submitted! "
