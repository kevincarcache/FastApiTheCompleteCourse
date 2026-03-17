from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

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
    id: Optional[int] = Field(description="ID is not required when creating a new book, it will be assigned automatically.", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, le=5)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "The Power of Habit",
                "author": "Charles Duhigg",
                "description": "A book about the science of habit formation and how to change habits.",
                "rating": 5
            }
        }

    }

BOOKS = [
    Book(1, "Atomic Habits", "James Clear", "A practical guide to building good habits and breaking bad ones.", 5),
    Book(2, "The 5 Second Rule", "Mel Robbins", "A simple method to stop hesitation and take action quickly.", 5),
    Book(3, "The Let Them Theory", "Mel Robbins", "A mindset for letting go of control and focusing on what truly matters.", 5),
    Book(4, "The Mountain Is You", "Brianna Wiest", "A book about self-sabotage and personal transformation.", 5),
    Book(5, "Think Like a Monk", "Jay Shetty", "Lessons on peace, purpose, and clarity inspired by monk life.", 5),
    Book(6, "The Subtle Art of Not Giving a F*ck", "Mark Manson", "A direct approach to living with intention and better values.", 5),
    Book(7, "You Are a Badass", "Jen Sincero", "Motivational advice to build confidence and improve your life.", 5),
    Book(8, "Can't Hurt Me", "David Goggins", "A memoir and mindset guide about discipline and mental toughness.", 5),
    Book(9, "Ikigai", "Hector Garcia and Francesc Miralles", "An exploration of purpose, balance, and living well.", 5),
    Book(10, "Make Your Bed", "Admiral William H. McRaven", "Life lessons about discipline, resilience, and small daily actions.", 5),
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}")
async def read_book(book_id: int = Path(gt=0, description="The ID of the book to retrieve.")):
    for book in BOOKS:
        if book.id == book_id:
            return book

    raise HTTPException(status_code=404, detail="Book not found.")    

@app.get("/books/")
async def read_books_by_rating(rating: int = Query(gt=0, le=5, description="The rating of the books to filter by.")):
    return [book for book in BOOKS if book.rating == rating]

@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_book(new_book: BookRequest):
    book = Book(**new_book.model_dump())
    BOOKS.append(assign_book_id(book))

def assign_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1

    return book

@app.put("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(updated_book: BookRequest, book_id: int = Path(gt=0, description="The ID of the book to update.")):
    for index, book in enumerate(BOOKS):
        if book.id == book_id:
            updated_book_data = updated_book.model_dump()
            updated_book_data["id"] = book_id
            BOOKS[index] = Book(**updated_book_data)
            return

    raise HTTPException(status_code=404, detail="Book not found.")

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0, description="The ID of the book to delete.")):
    for index, book in enumerate(BOOKS):
        if book.id == book_id:
            del BOOKS[index]
            return

    raise HTTPException(status_code=404, detail="Book not found.")