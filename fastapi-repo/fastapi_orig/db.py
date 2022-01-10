import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# セキュア文字列は環境変数から取得する
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')

# 接続情報URIを生成
SQLALCHEMY_DATABASE_URL = 'mysql://{}:{}@{}:3306/{}?charset=utf8'.format(DB_USER, DB_PASS, DB_HOST, DB_NAME)

# サポートしているDBと対話するためのエンジン
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# DBに接続するためのセッション作成
SessionLocal = sessionmaker(bind=engine)

# declarativeメタクラス
Base = declarative_base()

# 依存性の注入
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


