from typing import List, Optional
from fastapi import APIRouter, HTTPException
from sqlmodel import  Session
from db import engine
from sqlalchemy import MetaData
import heroes.model as model
import heroes.crud as crud
import common.model as common_model

router = APIRouter()

table_name = 'heroes'

# メタ情報取得
@router.get("/"+table_name+"/meta", response_model=List[common_model.Meta])
def get_table_columns():
    meta = []

    m = MetaData()
    m.reflect(engine)
    for col in m.tables[table_name].columns:
        meta.append( {
            'column_name': m.tables[table_name].c[col.name].name,
            'column_type': str(m.tables[table_name].c[col.name].type),
            'column_primary_key': m.tables[table_name].c[col.name].primary_key,
            'column_autoincrement': True if (m.tables[table_name].c[col.name].autoincrement == True) else False ,
            'column_nullable': m.tables[table_name].c[col.name].nullable,
        })

    return meta


# レコード数取得
@router.get("/"+table_name+"/count", response_model=common_model.Count)
def get_count(
    id: Optional[str] = None,
    name: Optional[str] = None,
    secret_name: Optional[str] = None,
    age: Optional[str] = None,
):
    with Session(engine) as session:
        return crud.get_count(session,id,name,secret_name,age)


# 特定の１レコード表示
@router.get("/"+table_name+"/{id}", response_model=model.heroesRead)
def read_hero(id: int):
    with Session(engine) as session:
        db_hero = crud.get_hero_by_id(session, id)
        if db_hero is None:
            raise HTTPException(status_code=404, detail="id not found")
        return db_hero

# 検索
@router.get("/"+table_name+"/", response_model=List[model.heroesRead])
def read_heroes(skip: int = 0, limit: int=10,
    id: Optional[str] = None,
    name: Optional[str] = None,
    secret_name: Optional[str] = None,
    age: Optional[str] = None,
):
    with Session(engine) as session:
        return crud.get_heroes(session,skip,limit,
id,
name,
secret_name,
age,
)


# 新規作成
@router.post("/"+table_name+"/", response_model=model.heroesRead)
def create_hero(hero: model.heroesCreate):
    with Session(engine) as session:
        return crud.create_hero(session, hero)


# 更新（PUTによる全フィールド更新）
@router.put("/"+table_name+"/{id}", response_model=model.heroesRead)
def update_hero(id: int, hero: model.heroesBase):
    with Session(engine) as session:
        db_hero = crud.get_hero_by_id(session,id)
        if db_hero is None:
            raise HTTPException(status_code=404, detail="id not found")
        return crud.update_hero(session,hero,db_hero)


# 更新（Patchによるフィールド更新）
@router.patch("/"+table_name+"/{id}", response_model=model.heroesRead)
def patch_hero(id: int, hero: model.heroesPatch):
    with Session(engine) as session:
        db_hero = crud.get_hero_by_id(session,id)
        if db_hero is None:
            raise HTTPException(status_code=404, detail="id not found")
        return crud.patch_hero(session,hero,db_hero)


# 削除
@router.delete("/"+table_name+"/{id}", response_model=model.heroesRead)
def delete_hero(id: int):
    with Session(engine) as session:
        db_hero = crud.get_hero_by_id(session, id)
        if db_hero is None:
            raise HTTPException(status_code=404, detail="id not found")

        return crud.delete_hero(session, db_hero)
