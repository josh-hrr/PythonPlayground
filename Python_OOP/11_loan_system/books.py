from typing import Protocol
from exceptions import BookIsNotAvailableError
from abc import ABC, abstractmethod

class BookProtocol(Protocol):
  def is_lend_book(self) -> str:
    """Method to lend a book"""
    ...

  def is_return_book(self) -> str:
    """Method to return a book"""
    ...

class BookBase(ABC):
  @abstractmethod
  def is_lend_book(self) -> str:
    ...

  @abstractmethod
  def is_return_book(self) -> str:
    ...

  @abstractmethod
  def is_popular_book(self) -> bool:
    ...

class Book(BookBase):
  def __init__(self, title: str, author: str, isbn: str, available: bool = True): 
    self.title = title
    self.author = author
    self.isbn = isbn
    self.available = available
    self.__times_lent = 0

  @classmethod
  def create_book_unavailable(cls, title: str, author: str, isbn: str):
    return cls(title, author, isbn, available=False)

  def __str__(self):
    return f"Title: {self.title}, Author: {self.author}, Availability: {self.available}, Times_Lent: {self.times_lent}"
  
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

  def is_popular_book(self) -> bool:
    return self.__times_lent > 5
  
  '''
  #getter and setters.
  - getters in pyhon use the @property decorator
  - setters in python use the @getter_name_method.setter decorator
  '''
  @property
  def times_lent(self) -> int:
    return self.__times_lent
  
  @times_lent.setter
  def times_lent(self, times_lend: int):
    if times_lend > 0:
      self.__times_lent = times_lend
    else:
      raise ValueError("The value times_lent must be greater than zero")
  

  
class BookPhysical(Book):
  def get_calculate_duration(self):
    return "7 days"
  
class BookDigital(Book):
  def get_calculate_duration(self):
    return "14 days"
  
