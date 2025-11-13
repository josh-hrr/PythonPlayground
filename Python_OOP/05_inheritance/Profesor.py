from Usuario import Usuario

class Profesor(Usuario):
  def __init__(self, name, DPI):
    super().__init__(name, DPI)
    self.book_limit = None

  def request_book(self, title):
    self.books_borrowed.append(title)
    return f"The book {title} has been authorized!"