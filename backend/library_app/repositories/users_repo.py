from backend.library_app.models import Users
from sqlalchemy import select
from typing import Optional, List
from backend.library_app.schemas import CreateUser
from sqlalchemy.orm import Session

class UsersRepo:

    def __init__(self, db:Session):
        self.db = db

    def get_all(self) -> List[Users]:
        return self.db.execute(select(Users)).scalars().all()

    def get_by_id(self, user_id: int) -> Optional[Users]:
        return self.db.execute(select(Users).where(Users.id == user_id)).scalars().first()

    def get_by_name(self, user_name: str) -> List[Users]:
        return self.db.execute(select(Users).where(Users.name == user_name)).scalars().all()

    def get_by_login(self, user_login: str) -> Optional[Users]:
        return self.db.execute(select(Users).where(Users.login == user_login)).scalars().first()

    def create(self, user_data: CreateUser) -> Users:
        db_user = Users(**user_data.model_dump(exclude=True))
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

