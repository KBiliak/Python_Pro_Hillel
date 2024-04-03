from pydantic import BaseModel, ValidationError, constr

class BookModel(BaseModel):
    name: constr(min_length=3, max_length=30)
    author: str
    year: int


class Book:
    def __init__(self, book_model: BookModel):
        self.book_model = book_model

    def book_info(self):
        return f"Book: {self.book_model.name}, Author: {self.book_model.author}, Year: {self.book_model.year}"

try:
    book_data = {"name": "Dune", "author": "Frank Herbert", "year": 1965}
    book_model = BookModel(**book_data)
    book = Book(book_model)
    print(book.book_info())

except ValidationError as e:
    print("Validation error:", e)
