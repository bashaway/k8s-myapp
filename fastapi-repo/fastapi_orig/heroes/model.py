from typing import List, Optional
from sqlmodel import Field, SQLModel

# None
#   Pydantic : Optional
#   SQLAlchemy : nullable
#
# PUT/PATCHでのnull更新時はnullを送信する

class heroesBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)


class heroesCreate(heroesBase):
    pass


class heroes(heroesBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class heroesRead(heroesBase):
    id: int


class heroesPatch(SQLModel):
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None
