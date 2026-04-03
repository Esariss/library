from os.path import exists

from backend.library_app.models import Borrow, Books
from sqlalchemy import select, update, delete
from typing import Optional, List
from backend.library_app.schemas import CreateBook, CreateBorrow, UpdateBook
from sqlalchemy.orm import Session

class BooksRepo:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Books]:
        return self.db.execute(select(Books)).scalars().all()

    def get_inventory_count(self, book_id: int) ->  int:
        return int(self.db.execute(select(Books.inventory).where(Books.id == book_id)).scalar().first())

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

    def update(self, book_id: int, book_data: UpdateBook) -> Optional[Books]:
        updating = self.db.execute(update(Books).where(Books.id == book_id).values(**book_data.model_dump(exclude_unset=True)).returning(Books)).scalar_one_or_none()
        self.db.commit()
        return updating

    def delete(self, book_id: int) -> Optional[Books]:
        deleting = self.db.execute(delete(Books).where(Books.id == book_id).returning(Books)).scalar_one_or_none()
        self.db.commit()
        return deleting

    def title_exists(self, title: str) -> bool:
        return self.db.execute(select(exists(Books).where(Books.title == title))).scalar()

    def id_exist(self, book_id: int) -> bool:
        return self.db.execute(select(exists(Books).where(Books.id == book_id))).scalar()

    def minus_inventory(self, book_id: int, minus: int = 1) -> Optional[Books]:
        updating = self.db.execute(update(Books).where(Books.id == book_id, Books.inventory >= minus).values(inventory= Books.inventory - minus).returning(Books)).scalar_one_or_none()
        self.db.commit()
        return updating

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

    def delete(self, borrow_id: int) -> Optional[Borrow]:
        deleting = self.db.execute(delete(Borrow).where(Borrow.id == borrow_id).returning(Borrow)).scalar_one_or_none()
        self.db.commit()
        return deleting

    def id_exist(self, borrow_id: int) -> bool:
        return self.db.execute(select(exists(Borrow).where(Borrow.id == borrow_id))).scalar()

    def book_id_exist(self, book_id: int) -> bool:
        return self.db.execute(select(exists(Borrow).where(Borrow.book_id == book_id))).scalar()

    def user_id_exist(self, user_id: int) -> bool:
        return self.db.execute(select(exists(Borrow).where(Borrow.user_id == user_id))).scalar()

