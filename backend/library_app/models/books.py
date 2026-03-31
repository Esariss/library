from sqlalchemy.orm import Mapped, mapped_column
from backend.database import Base
from sqlalchemy import Text

class Books(Base):

    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column(Text)
    first_count: Mapped[int]
    inventory: Mapped[int]


class Borrow(Base):

    __tablename__ = "borrows"

    id : Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))

    borrowed_at: Mapped[datetime] = mapped_column(default= lambda : datetime.now(timezone.utc))
