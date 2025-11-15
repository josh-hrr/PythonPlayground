from Estudiante import Estudiante
from Profesor import Profesor
from RequestorProtocol import RequestorProtocol
from Exceptions import LibraryError


if __name__ == "__main__":
  estudent1 = Estudiante("Estudent1", "123", "career1")
  profesor1 = Profesor("Prof1", "456")
  profesor2 = Profesor("Prof2", "123")

  print(estudent1.request_book("Python Test1"))
  print(estudent1.request_book("Python Test2")) 
  print(estudent1.request_book("Python Test3"))
  print(estudent1.request_book("Python Test4"))

  print(estudent1.return_book("Python Test3"))
  print(estudent1.get_books_requested())

  #Profesor does not implement the methods required by RequestorProtocol
  #It does not satisfy the Protocol contract.
  #This is similar to how a class must implement all methods of a Java interface.

  profesor_list: list[RequestorProtocol] = [profesor1, profesor2]  
  print(f"printing professor_list: {profesor_list}")
  
  try:
    print(estudent1.request_book(False))
  except LibraryError as e:
    print(f"{e}, {type(e)}")
    print("Error: We couldn't request the book") 
  print("##code continues to execute")

  #Excercise
  try:
    print(estudent1.return_book(None))
  except LibraryError as e:
    print(f"{e}, {type(e)}")
    print("Error: We coudn't return the book")
  print("##code continues to execute")


