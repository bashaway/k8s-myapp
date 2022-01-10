from typing import List, Optional
from pydantic import BaseModel, Field

# 件数取得は件数のみを取得する
class Count(BaseModel):
    count: int

# カラム情報
class Meta(BaseModel):
    column_name: str
    column_type: str
    column_primary_key: bool
    column_autoincrement: bool
    column_nullable: bool

