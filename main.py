import logging
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db
from models import Base
from schemas import Book, BookCreate, BookUpdate
from crud import create_book, get_books, get_book, update_book_quantity, delete_book as delete_book_crud

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/books/", response_model=Book)
def create_book_endpoint(book: BookCreate, db: Session = Depends(get_db)):
    logger.info("Creating a new book")
    try:
        return create_book(db=db, book=book)
    except Exception as e:
        logger.error(f"Error creating book: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/books/", response_model=list[Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    logger.info("Fetching books")
    try:
        books = get_books(db, skip=skip, limit=limit)
        return books
    except Exception as e:
        logger.error(f"Error fetching books: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/books/{book_id}", response_model=Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    logger.info(f"Fetching book with ID {book_id}")
    try:
        db_book = get_book(db, book_id=book_id)
        if db_book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        return db_book
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error fetching book: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, quantity: BookUpdate, db: Session = Depends(get_db)):
    logger.info(f"Updating book with ID {book_id}")
    try:
        return update_book_quantity(db=db, book_id=book_id, quantity=quantity.quantity)
    except Exception as e:
        logger.error(f"Error updating book: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.delete("/books/{book_id}", response_model=Book)
def delete_book_endpoint(book_id: int, db: Session = Depends(get_db)):
    logger.info(f"Deleting book with ID {book_id}")
    try:
        db_book = get_book(db, book_id=book_id)
        if db_book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        return delete_book_crud(db=db, book_id=book_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error deleting book: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
