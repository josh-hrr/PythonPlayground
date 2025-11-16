from books import Book
from users import Student, Profesor
from exceptions import UserNotFoundError, BookIsNotAvailableError

class Library:
  def __init__(self, name: str) -> None:
    self.name = name
    self.books: list[Book] = []
    self.users: list[Student | Profesor] = []

  def get_books_available(self):
    return [book for book in self.books if book.available]
  
  def search_user_by_dpi(self, dpi: str):
    for user in self.users:
      if user.DPI == dpi:
        return user
    raise UserNotFoundError(f"User with the: {dpi} was not found!")
  
  def search_book_by_title(self, title: str):
    for book in self.books:
      if book.title == title and book.available:
        return book
    raise BookIsNotAvailableError(f"Book with title: {title} was not found!")
  
  @staticmethod
  def validate_isbn(isbn: str):
    return len(isbn) >= 10