'''
Protocol:
allows to have: 
- interface without inheritance
- static typing
- contracts

'''

from typing import Protocol

class RequestorProtocol(Protocol):
  def request_book(self, title: str) -> str:
    """Method must be implemented for any requestor"""
    ...

  def get_poly_example(self) -> str:
    """Method must be implemented for any requestor"""
    ...