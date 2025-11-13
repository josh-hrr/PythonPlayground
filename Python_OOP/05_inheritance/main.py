from Estudiante import Estudiante
from Profesor import Profesor

if __name__ == "__main__":
  estudent1 = Estudiante("Estudent1", "123", "career1")
  profesor1 = Profesor("Prof1", "456")

  print(estudent1.request_book("Python Test1"))
  print(estudent1.request_book("Python Test2")) 
  print(estudent1.request_book("Python Test3"))
  print(estudent1.request_book("Python Test4"))


