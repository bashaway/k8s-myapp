import json
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base, engine

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    email = Column(String(32), unique=True, index=True)
    group_id = Column(Integer, ForeignKey("groups.id"))

    # モデル化されたものをjsonデータに変換
    def model_to_json(self):
        return  {'id': self.id, 'name': self.name, "email": self.email, "group_id": self.group_id}
