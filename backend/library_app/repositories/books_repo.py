from backend.library_app.models import Borrow, Books
from sqlalchemy import select
from typing import Optional, List
from backend.library_app.schemas import CreateBook, CreateBorrow
from sqlalchemy.orm import Session

class BooksRepo:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Books]:
        return self.db.execute(select(Books)).scalars().all()

    def get_by_id(self, book_id: int) -> Optional[Books]:
        return self.db.execute(select(Books).where(Books.id == book_id)).scalars().first()

    def get_by_title(self, book_title: str) -> Optional[Books]:
        return self.db.execute(select(Books).where(Books.title == book_title)).scalars().first()

    def create(self, book_data: CreateBook) -> Books:
        db_book = Books(**book_data.model_dump())
        self.db.add(db_book)
        self.db.commit()
        self.db.refresh(db_book)
        return db_book

class BorrowRepo:
    def __init__(self, db:Session):
        self.db = db

    def get_all(self) -> List[Borrow]:
        return self.db.execute(select(Borrow)).scalars().all()

    def get_by_id(self, borrow_id: int) -> Optional[Borrow]:
        return self.db.execute(select(Borrow).where(Borrow.id == borrow_id)).scalars().first()

    def get_by_user_id(self, user_id: int) -> List[Borrow]:
        return self.db.execute(select(Borrow).where(Borrow.user_id == user_id)).scalars().all()

    def get_by_book_id(self, book_id: int) -> List[Borrow]:
        return self.db.execute(select(Borrow).where(Borrow.book_id == book_id)).scalars().all()

    def create(self, borrow_data: CreateBorrow) -> Borrow:
        db_borrow = Borrow(**borrow_data.model_dump())
        self.db.add(db_borrow)
        self.db.commit()
        self.db.refresh(db_borrow)
        return db_borrow
