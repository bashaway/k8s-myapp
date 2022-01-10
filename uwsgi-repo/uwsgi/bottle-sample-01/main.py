#!/usr/bin/env python3
from bottle import Bottle,  run , default_app , static_file , request, HTTPResponse
from bottle import route, get, post, put, delete
from bottle import jinja2_template as template
import os


path_prefix = '/uwsgi/bottle-sample-01'


# TEMPLATE_PATHにテンプレートファイルをいれておく
# デフォルトは ./ と ./views の２つ
#bottle.TEMPLATE_PATH += ['./xxx']


param_json = {}
param_json['groups'] = [
    {'key': 'value1',  'flg': False },
    {'key': 'value2',  'flg': True },
    {'key': 'value3',  'flg': False },
]

param_list = [10,20,50,100]

@get(path_prefix+'/')
def index():
    return template('index.html', {'param_json': param_json, 'param_list': param_list})


# 動的ルーティングする場合はOptionalができないので
# 「なし」ルートを直前に持ってくることでデフォルト引数をとる
@get(path_prefix+'/hello/')
@get(path_prefix+'/hello/<name>')
def hello(name="Stranger"):
    return template('Hello {{name}}, how are you!?', name=name)


# 正規表現で空マッチを組めばパスパラメータなしでもよいが
# この場合は空でマッチしてしまうためデフォルト引数はとれない
@get(path_prefix+'/regex/<input:re:[a-z]*>')
def regex(input):
    return template('input value : {{input}}', input=input)


# content-typeを指定してjsonとして返すこともできる
@get(path_prefix+'/json/')
@get(path_prefix+'/json/<id:int>/<name>')
def json(id=999,name='default_name'):
    body = {"status_code": 200, "message": "json_response", "id": id, "name": name}
    response = HTTPResponse(status=200, body=body)
    response.set_header("Content-Type", "application/json")
    return response




# リクエストパスが/static/hoge.js なら./static/hoge.jsを戻す
@get(path_prefix+'/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static/')

if __name__ == '__main__':
    run(host='0.0.0.0', port=8081)
else:
    application = default_app()

