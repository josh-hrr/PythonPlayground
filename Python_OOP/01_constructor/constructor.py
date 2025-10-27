import threading

class Book:
  _next_id = 1
  _lock = threading.Lock()

  def __init__(self, name, description, availability, ssn=1): 
    with Book._lock:
      self.id = Book._next_id
      Book._next_id += 1 
    self.name = name
    self.description = description
    self.ssn = ssn
    self.availability = availability 

book1 = Book("name1", "description1", True)
book2 = Book("name2", "description2", False)
book3 = Book("name3", "description3", True)

 

print(f"book1: {book1.id}, {book1.name}")
print(f"book2: {book2.id}, {book2.name}")
 

print("\nCatalog: \n")


catalog = []
for book in (book1, book2, book3):
  catalog.append({
    "id": book.id,
    "name": book.name,
    "description": book.description,
    "availability": book.availability
  })
  

print(catalog)

#test