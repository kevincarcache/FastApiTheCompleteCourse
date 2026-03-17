from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Atomic Habits', 'author': 'James Clear', 'category': 'self-help'},
    {'title': 'The 5 Second Rule', 'author': 'Mel Robbins', 'category': 'self-help'},
    {'title': 'The Let Them Theory', 'author': 'Mel Robbins', 'category': 'self-help'},
    {'title': 'The Mountain Is You', 'author': 'Brianna Wiest', 'category': 'self-help'},
]

@app.get('/books')
async def read_all_books():
    return BOOKS

@app.get('/books/{book_title}')
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book

@app.get('/books/')
async def read_book_by_category(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.post('/books/create_book')
async def create_new_book(new_book=Body()):
    BOOKS.append(new_book)
