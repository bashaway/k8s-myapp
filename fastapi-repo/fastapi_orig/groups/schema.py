from typing import List, Optional
from pydantic import BaseModel


# patch用にOptionalで属性を定義
class GroupPatch(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


# データの作成および読み取りで使用する共通の属性
class GroupBase(BaseModel):
    name: str
    description: str


# データの作成時に使用 idといった作成時には不要なものを持たない
class GroupCreate(GroupBase):
    pass


# データ読み取り時に使用
class Group(GroupBase):
    id: int

    # ORMを使用する
    class Config:
        orm_mode = True
