from library import Library
import json
from datetime import datetime 
from books import Book
from users import Student, Profesor

class Persistency:
    def __init__(self, file: str ="library.json") -> None:
        self.file = file

    def save_data(self, library: Library):
        data: dict[str, object] = {
            "name": library.name,
            "users": [
                user.__dict__
                for user in library.users
                ],
            "books": [
                book.__dict__
                for book in library.books
            ],
            "date_saved": datetime.now().isoformat()
        }
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load_data(self):
        with open(self.file, "r", encoding="utf-8") as f:
            data = json.load(f) 
        library = Library(data["name"])
        for book_data in data["books"]: 
            book = Book(
                title=book_data['title'],
                author=book_data['author'],
                isbn=book_data['isbn'],
                available=book_data['available']
                )
            library.books.append(book)
    #data loaded:  {'name': 'Hans', 'DPI': '1', 'books_borrowed': [], 'career': 'Engineering', 'email': None, 'book_limit': 3}
        for user_data in data["users"]:
            if "career" in user_data: 
                user = Student(
                    name=user_data['name'],
                    DPI=user_data['DPI'], 
                    career=user_data['career']
                )
            else:
                user = Profesor(
                    name=user_data['name'],
                    DPI=user_data['DPI'],
                )
            library.users.append(user)
        return library