from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from backend.database import Base
from datetime import datetime, timezone

class Borrow(Base):

    __tablename__ = "borrows"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))

    borrowed_at: Mapped[datetime] = mapped_column(default= lambda : datetime.now(timezone.utc))

