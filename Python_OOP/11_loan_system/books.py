from typing import Protocol
from exceptions import BookIsNotAvailableError

class BookProtocol(Protocol):
  def is_lend_book(self) -> str:
    """Method to lend a book"""
    ...

  def is_return_book(self) -> str:
    """Method to return a book"""
    ...
    
class Book:
  def __init__(self, title: str, author: str, isbn: str, available: bool = True): 
    self.title = title
    self.author = author
    self.isbn = isbn
    self.available = available
    self.__times_lent = 0

  def __str__(self):
    return f"Title: {self.title}, Author: {self.author}, Availability: {self.available}"
  
  def is_lend_book(self) -> str:
    if not self.available:
      raise BookIsNotAvailableError(f"'{self.title}' is not available")
    if self.available:
      self.available = False
      self.__times_lent += 1
      return f"'{self.title}' was lent successfully! Total books lent: {self.__times_lent}"
    return "Error in lending the book"

  def is_return_book(self) -> str:
    self.available = True
    return f"'{self.title}' has been returned, the book is available again."
    return "Error in returning the book"

  def is_popular_book(self):
    return self.__times_lent > 5
  
class BookPhysical(Book):
  def get_calculate_duration(self):
    return "7 days"
  
class BookDigital(Book):
  def get_calculate_duration(self):
    return "14 days"
  
