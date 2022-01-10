from typing import List, Optional
from pydantic import BaseModel, Field


# patchは全部の要素があるわけではないのでOptionalにするみたい。。。
class UserPatch(BaseModel):
    name: Optional[str] = Field(None, example="Alice", description="氏名")
    email: Optional[str] = Field(None, example="alice@example.com", description="メールアドレス")
    group_id: Optional[int] = Field(None, example=1, description="グループID")


# データの作成および読み取りで使用する共通の属性
class UserBase(BaseModel):
    name: str     = Field(example="Alice", description="氏名")
    email: str    = Field(example="alice@example.com", description="メールアドレス")
    group_id: int = Field(example=1, description="グループID")


# データの作成時に使用 idといった作成時には不要なものを持たない
class UserCreate(UserBase):
    pass


# データ読み取り時に使用
class User(UserBase):
    id: int

    # ORMを使用する
    class Config:
        orm_mode = True
