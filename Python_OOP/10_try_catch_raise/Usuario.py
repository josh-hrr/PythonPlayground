class Usuario:
  def __init__(self, name: str, DPI: str):
    self.name = name
    self.DPI = DPI 
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