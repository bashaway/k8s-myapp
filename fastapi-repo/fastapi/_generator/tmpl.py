#!/usr/bin/env python3
import os, json, shutil
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from jinja2 import Environment, FileSystemLoader


# セキュア文字列は環境変数から取得する
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')

# 接続情報を生成
SQLALCHEMY_DATABASE_URL = 'mysql://{}:{}@{}:3306/{}?charset=utf8'.format(DB_USER, DB_PASS, DB_HOST, DB_NAME)

# DB接続エンジン
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# メタ情報の取得
m = MetaData()
m.reflect(engine)

# テーブル全体のメタ情報
metas = {}

# テンプレート置き場の設定
os.chdir(os.path.dirname(__file__))
env = Environment(
    loader=FileSystemLoader(os.getcwd()),
    trim_blocks=True
)
os.chdir('../')

# main.pyを生成
# テーブルごとにグルーピングする必要があるのでテンプレート化する
model_template = env.get_template('main.py.tmpl')
model_result = model_template.render(tables=m.tables)
with open('./main.py', 'w') as f:
    f.write(model_result)


# メタ情報をテーブルごとに拾っていく
for table in m.tables:
    table_name=table

    meta = []
    for col in m.tables[table_name].columns:
        # メタ情報をテーブルごとに拾っていく
        meta.append( {
            'column_name': m.tables[table_name].c[col.name].name,
            'column_type': str(m.tables[table_name].c[col.name].type),
            'column_primary_key': m.tables[table_name].c[col.name].primary_key,
            'column_autoincrement': True if (m.tables[table_name].c[col.name].autoincrement == True) else False ,
            'column_nullable': m.tables[table_name].c[col.name].nullable,
        })
    metas[table_name]=meta


    # テーブルをディレクトリとして生成
    # すでに存在していれば削除してから生成
    dir_path = './'+table_name
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
    os.mkdir(dir_path)

    # テーブル名/router.pyを生成
    router_template = env.get_template('router.py.tmpl')
    router_result = router_template.render(table_name=table_name,meta=meta)
    with open(dir_path+'/router.py', 'w') as f:
        f.write(router_result)

    # テーブル名/crud.pyを生成
    crud_template = env.get_template('crud.py.tmpl')
    crud_result = crud_template.render(table_name=table_name,meta=meta)
    with open(dir_path+'/crud.py', 'w') as f:
        f.write(crud_result)

    # テーブル名/model.pyを生成
    model_template = env.get_template('model.py.tmpl')
    model_result = model_template.render(table_name=table_name,meta=meta)
    with open(dir_path+'/model.py', 'w') as f:
        f.write(model_result)


# 全部のメタ情報を出力するときはコレで
#print(json.dumps(metas,indent=4))

