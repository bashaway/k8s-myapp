import os
from sqlalchemy import create_engine

# セキュア文字列は環境変数から取得する
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')

# 接続情報を生成
SQLALCHEMY_DATABASE_URL = 'mysql://{}:{}@{}:3306/{}?charset=utf8'.format(DB_USER, DB_PASS, DB_HOST, DB_NAME)

# DB接続エンジン
engine = create_engine(SQLALCHEMY_DATABASE_URL)

