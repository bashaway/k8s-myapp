#!/usr/bin/env python3
from bottle import Bottle,  run , default_app , static_file , request, HTTPResponse
from bottle import route, get, post, put, delete
from bottle import jinja2_template as template
import os


path_prefix = '/uwsgi/bottle-sample-02'


@get(path_prefix+'/')
def index():
    return template('index.html')


# リクエストパスが/static/hoge.js なら./static/hoge.jsを戻す
@get(path_prefix+'/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static/')

if __name__ == '__main__':
    run(host='0.0.0.0', port=8081)
else:
    application = default_app()

