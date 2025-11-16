from books import Book
from users import User
from exceptions import UserNotFoundError

class Library:
  def __init__(self, name: str) -> None:
    self.name = name
    self.books: list[Book] = []
    self.users: list[User] = []

  def get_books_available(self):
    return [book for book in self.books if book.available]
  
  def search_user_by_dpi(self, dpi: str):
    for user in self.users:
      if user.DPI == dpi:
        return user
    raise UserNotFoundError(f"User with the: {dpi} was not found!")
  
