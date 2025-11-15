from Usuario import Usuario

class Profesor(Usuario):
  def __init__(self, name: str, DPI: str):
    super().__init__(name, DPI)
    self.book_limit = None
 
  def request_book(self, title:str) -> str:
    self.books_borrowed.append(title)
    return f"The book {title} has been authorized!" 
   
  def get_poly_example(self) -> str: 
    return "Poly example from professor!" 