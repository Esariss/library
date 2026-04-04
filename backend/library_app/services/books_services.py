from backend.library_app.repositories.books_repo import BooksRepo, BorrowRepo
from fastapi import HTTPException

class BooksService:
    def __init__(self, repo: BooksRepo):
        self.repo = repo

    def get_all_books(self):
        return self.repo.get_all()

    def get_by_id(self, book_id: int):
        result = self.repo.get_by_id(book_id)
        if result:
            return result
        raise HTTPException(status_code=404, detail="book not found")

    def get_by_title(self, book_title: str):
        result = self.repo.get_by_title(book_title)
        if result:
            return
        raise HTTPException(status_code=404, detail="book not found")

    def get_inventory_count(self, book_id):
        if self.repo.id_exist(book_id):
            return self.repo.get_inventory_count(book_id)
        raise HTTPException(status_code=404, detail="that id is not exist")

    def create(self, book_data):
        if self.repo.title_exists(book_data.title):
            raise HTTPException(status_code=409, detail="that title is already exists")
        return book_data

    def delite(self, book_id: int):
        return self.repo.delete(book_id)

    def update(self, book_id: int, book_data):
        if self.repo.id_exist(book_id):
            return self.repo.update(book_id, book_data)
        raise HTTPException(status_code=404, detail="that id is not exists")

    def minus_inventory(self, book_id: int, minus: int = 1):
        if self.repo.id_exist(book_id) and self.repo.get_inventory_count(book_id) >= minus:
            return self.repo.minus_inventory(book_id, minus)
        raise HTTPException(status_code=404, detail="that id is not exist")

    def plus_inventory(self, book_id: int, plus: int = 1):
        if self.repo.id_exist(book_id):
            return self.repo.plus_inventory(book_id, plus)
        raise HTTPException(status_code=404, detail="that id is not exist")



class BorrowService:
    def __init__(self, repo: BorrowRepo ):
        self.repo = repo

    def get_all_borrows(self):
        return self.repo.get_all()

    def get_by_id(self, borrow_id: int):
        if self.repo.id_exist(borrow_id):
            return self.repo.get_by_id(borrow_id)
        raise HTTPException(status_code=404, detail="that id is not exist")

    def get_by_book_id(self, book_id: int):
        if self.repo.get_by_book_id(book_id):
            return self.repo.get_by_book_id(book_id)
        raise HTTPException(status_code=404, detail="that id is not exist")

    def get_by_user_id(self, user_id: int):
        if self.repo.user_id_exist(user_id):
            return self.repo.get_by_user_id(user_id)
        raise HTTPException(status_code=404, detail="that id is not exist")

    def delete(self, borrow_id: int):
        return self.repo.delete(borrow_id)

    def create(self, borrow_data):
        book_service = BooksService(BooksRepo)
        if not self.repo.is_gave_back(borrow_data.user_id, borrow_data.book_id):
            raise HTTPException(status_code=409, detail="At first return the book")
        if book_service.get_inventory_count(borrow_data.book_id) == 0:
            raise HTTPException(status_code=422, detail="no books in inventory")
        book_service.minus_inventory(borrow_data.book_id)
        return self.repo.create(borrow_data)

    def gave_back(self, user_id: int, book_id: int):
        book_service = BooksService(BooksRepo)
        if self.repo.is_gave_back(user_id, book_id):
            raise HTTPException(status_code=409, detail="you already return the book")
        book_service.plus_inventory(book_id)
        return self.repo.update_gave_back(user_id, book_id)



