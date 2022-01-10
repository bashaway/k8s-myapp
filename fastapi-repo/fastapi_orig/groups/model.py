import json
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db import Base, engine


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    description = Column(String(200))

    # 外部キーとして参照されているレコードを削除しようとすると
    # 参照している側のフィールドをNullに変更してから親側レコードを削除する
    # なので、SQLとしての外部キー制約にひっかからずに削除されてしまう
    # passive_deletes=TrueにしておくとNullにする処理をスキップするため
    # 親側レコード削除時に外部キー制約に引っかかって削除できないようになる
    user_relation = relationship("User",backref="groups", cascade="all, delete", passive_deletes=True)

    # モデル化されたものをjsonデータに変換
    def model_to_json(self):
        return  {'id': self.id, 'name': self.name, "description": self.description}
