
from users import Student, Profesor, User
from books import Book, BookPhysical, BookDigital
from library import Library 
from exceptions import UserNotFoundError


if __name__ == "__main__":

  my_library = Library("University Library") 
  student_1 = Student("Hans", "1", "Engineering")
  student_2 = Student("Rose", "2", "Psychology") 
  profesor_1 = Profesor("Prof1", "3")
  profesor_2 = Profesor("Prof2", "4") 
  book_1 = Book("Python Basics", "Author1", "123456")
  book_2 = Book("Advanced Python", "Author2", "7891011")
  book_3 = Book("Data Science with Python", "Author3", "12131415")
  physical_book_1 = BookPhysical("Physical Book1", "Author4", "16171819")
  digital_book_1 = BookDigital("Digital Book1", "Author5", "20212223")

  my_library.users = [student_1, student_2, profesor_1, profesor_2]  
  my_library.books = [book_1, book_2, book_3, physical_book_1, digital_book_1] 

  print("Welcome to My Library!") 
  print("Books available: ")
  for book in my_library.get_books_available():
    print(book)
  print("\n")
  dpi: str = input("Enter the DPI number: ")
  new_user: User
  user_found: bool = False

  try:
    new_user = my_library.search_user_by_dpi(dpi)
    user_found = True
    try: 
      print(new_user.name, new_user.DPI, new_user.career)
    except AttributeError:
      print(new_user.name, new_user.DPI)
      print(f"User {new_user.name} does not have a career attribute.") 
  except UserNotFoundError:
    print(f"User with DPI {dpi} not found in the system.") 
    user_found = False
 
 
