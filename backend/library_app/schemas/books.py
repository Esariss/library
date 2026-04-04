from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class CreateBook(BaseModel):
    title: str  = Field(..., description="Book title")
    description: str = Field(..., description="Book description")
    first_count: int = Field(..., description="Books count")

    model_config = ConfigDict(from_attributes=True)

class UpdateBook(BaseModel):
    title: Optional[str] = Field(None, description="Books title")
    description: Optional[str] = Field(None, description="Books description")
    inventory: Optional[int] = Field(None, description="Books in inventory")

    model_config = ConfigDict(from_attributes=True)

class ResponseBooks(BaseModel):
    id: int = Field(..., description="Books id")
    title: str = Field(..., description="Books title")
    description: str = Field(..., description="Books description")
    inventory: int = Field(..., description="Books in inventory")

    model_config = ConfigDict(from_attributes=True)


class CreateBorrow(BaseModel):
    user_id: int = Field(..., description="User_id")
    book_id: int = Field(..., description="Book id")


     