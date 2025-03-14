from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int

BOOKS = [
    Book(1, "Adicciones 1", "Kevin Carcache", "Excelente Libro", 5),
    Book(2, "Adicciones 2", "Kevin Carcache", "Excelente Libro", 5),
    Book(3, "Adicciones 3", "Kevin Carcache", "Excelente Libro", 5),
    Book(4, "Adicciones 4", "Kevin Carcache", "Excelente Libro", 5),
    Book(5, "Adicciones 5", "Kevin Carcache", "Excelente Libro", 5),
]

@app.get("/books/")
async def read_all_books():
    return BOOKS

@app.post("/books/")
async def create_book(new_book: BookRequest):
    book = Book(**new_book.model_dump())
    BOOKS.append(book)
