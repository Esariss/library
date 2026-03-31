from pydantic import BaseModel, Field
from typing import Optional

class CreateUser(BaseModel):
    name: str = Field(..., description="User name")
    lastname: str = Field(..., description="User lastname")
    login: str = Field(..., description="User login")

    model_config = ConfigDict(from_attributes=True)

class UpdateUser(BaseModel):
    name: Optional[str] = Field(None, description="User name")
    lastname: Optional[str] = Field(None, description="User lastname")
    login: Optional[str] = Field(None, description="User login")

    model_config = ConfigDict(from_attributes=True)

class ResponseUser(BaseModel):
    id: int = Field(..., description="User id")
    name: str = Field(..., description="User name")
    lastname: str = Field(..., description="User lastname")

    model_config = ConfigDict(from_attributes=True)
