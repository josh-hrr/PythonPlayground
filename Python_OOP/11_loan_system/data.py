from users import Student, Profesor 
from books import Book, BookPhysical, BookDigital

student_1 = Student("Hans", "1", "Engineering")
student_2 = Student("Rose", "2", "Psychology") 
student_3 = Student.create_student_with_email("Korean", "3", "Engineering", "test@test.com")
profesor_1 = Profesor("Prof1", "4")
profesor_2 = Profesor("Prof2", "5") 
book_1 = Book("Python Basics", "Author1", "123456")
book_2 = Book("Advanced Python", "Author2", "7891011")
book_3 = Book("Data Science with Python", "Author3", "12131415")
physical_book_1 = BookPhysical("Physical Book1", "Author4", "16171819")
digital_book_1 = BookDigital("Digital Book1", "Author5", "20212223")

student_data: list[Student] = [student_1, student_2, student_3]
profesor_data: list[Profesor] = [profesor_1, profesor_2]
book_data: list[Book] = [book_1, book_2, book_3, physical_book_1, digital_book_1]
