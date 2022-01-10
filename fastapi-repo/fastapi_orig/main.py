from typing import List
import os, re
from starlette.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, HTTPException , Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from db import SessionLocal, engine

path_prefix=os.getenv('FASTAPI_PATH_PREFIX')

app = FastAPI(
    title='FastAPI APPs',
    docs_url=path_prefix+'/docs',
    redoc_url=path_prefix+'/redoc',
    openapi_url=path_prefix+'/openapi.json',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # 許可するオリジンを設定
    #allow_origins=[
    #                  "http://PRODUCTION_SERVER",
    #              ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


templates = Jinja2Templates(directory="templates")


@app.get(path_prefix+"/")
def api_manager():

    tables = [
        'users',
        'groups',
        'heroes',
    ]
    table_info = []

    for name in tables:
 
        table_info.append( {
                'table_name': name,
                'base_path': path_prefix+'/'+name+'/',
                'meta_path': path_prefix+'/'+name+'/meta',
                'count_path': path_prefix+'/'+name+'/count',
               })

    return table_info

# グループごとにまとめる
import users.router as users_router
app.include_router(users_router.router,tags=["users"],prefix=path_prefix)

import groups.router as groups_router
app.include_router(groups_router.router,tags=["groups"],prefix=path_prefix)

import heroes.router as heroes_router
app.include_router(heroes_router.router,tags=["heroes"],prefix=path_prefix)


