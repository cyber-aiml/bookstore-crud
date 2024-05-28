from pydantic import BaseModel

class BookBase(BaseModel):
    name: str
    summary: str
    price: float
    quantity: int
    author: str

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    quantity: int

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
