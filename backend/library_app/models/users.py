from sqlalchemy.orm import Mapped, mapped_column
from backend.database import Base

class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    lastname: Mapped[str]
    login: Mapped[str] = mapped_column(unique=True, nullable=False)
