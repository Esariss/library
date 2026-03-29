from sqlalchemy.orm import Mapped, mapped_column
from backend.database import Base
from sqlalchemy import Text

class Books(Base):

    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[Text]
    first_count: Mapped[int]
    inventory: Mapped[int]




