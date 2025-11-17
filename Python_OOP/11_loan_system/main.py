
#from library import Library 
from exceptions import UserNotFoundError, BookIsNotAvailableError
#from data import student_data, profesor_data, book_data
from users import Student, Profesor
from books import Book
from persistency import Persistency

if __name__ == "__main__":


  #my_library = Library("University Library") 
  #my_library.users = []
  #my_library.users.extend(student_data)
  #my_library.users.extend(profesor_data)
  #my_library.books = book_data

  persistency = Persistency()
  my_library = persistency.load_data()


  print(f"Welcome to {my_library.name}!")  
  print("Books available: ")
  for book in my_library.get_books_available():
    print(book)
  print("\n")
  dpi: str = input("Enter the DPI number: ")
  user_found: Student | Profesor | None = None
  is_user_found: bool = False 
  try:
    user_found = my_library.search_user_by_dpi(dpi)
    is_user_found = True
    try: 
      print(user_found.name, user_found.DPI, user_found.career)
    except AttributeError:
      print(user_found.name, user_found.DPI)
      print(f"User {user_found.name} does not have a career attribute.") 
  except UserNotFoundError:
    print(f"User with DPI {dpi} not found in the system.") 
    is_user_found = False
  
  book_title: str = input("Enter book Title: ")
  book_found: Book | None = None
  is_book_found: bool = False
  try:
    book_found = my_library.search_book_by_title(book_title)
    is_book_found = True 
    print(f"Book found: {book_found.title}, {book_found.author}, {book_found.available}")
  except BookIsNotAvailableError:
    print(f"Book {book_title} not found!")
  
  if user_found is not None and book_found is not None and is_user_found and is_book_found: 
    result_request_book = user_found.request_book(book_found.title)
    print(f"\n{result_request_book}") 
    print("\n times lent test: ", book_found.times_lent) 
    print("\n set times lent test: ")
    book_found.times_lent = 50
    print("\n times lent test: ", book_found.times_lent) 
    try:
      result_is_lent_book = book_found.is_lend_book()
      print(f"\n{result_is_lent_book}")
    except BookIsNotAvailableError as e:
      print(e)

  #testing static method: 
  #print(Library.validate_isbn("1234567890"))

  create_book_unavailable = Book.create_book_unavailable("TitleTest", "Author Test", "123456")
  print("book is not available: ", create_book_unavailable)
  print("book is not available: ", create_book_unavailable.available)

  #save everytime there is a change
  persistency.save_data(my_library)
  
