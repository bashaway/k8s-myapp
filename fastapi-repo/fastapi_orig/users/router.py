from typing import List, Optional
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import MetaData
from db import get_db, engine
import common.model as common_model
import users.crud as crud
import users.schema as schema
import users.model as model

router = APIRouter()

table_name = 'users'

@router.get("/"+table_name+"/meta", response_model=List[common_model.Meta])
def get_table_columns(db: Session = Depends(get_db)):
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


@router.get("/"+table_name+"/count", response_model=common_model.Count)
def get_users_count(
                    id: Optional[str] = None,
                    name: Optional[str] = None,
                    email: Optional[str] = None,
                    group_id: Optional[str] = None,
                    db: Session = Depends(get_db),
                  ):

    return crud.get_users_count(db, id=id, name=name, email=email, group_id=group_id)


@router.get("/"+table_name+"/", response_model=List[schema.User])
def read_users(skip: int = 0,
               limit: int = 100,
               id: Optional[str] = None,
               name: Optional[str] = None,
               email: Optional[str] = None,
               group_id: Optional[str] = None,
               db: Session = Depends(get_db)):

    return crud.get_users(db, skip=skip, limit=limit, id=id, name=name, email=email, group_id=group_id)


@router.get("/"+table_name+"/{user_id}", response_model=schema.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/"+table_name+"/", response_model=schema.User)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@router.put("/"+table_name+"/{user_id}", response_model=schema.User)
def update_user( user_id: int, user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user(db, user, db_original=db_user)


@router.patch("/"+table_name+"/{user_id}", response_model=schema.User)
def patch_user(user_id: int, user: schema.UserPatch, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.patch_user(db, user, db_original=db_user)


@router.delete("/"+table_name+"/{user_id}", response_model=schema.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.delete_user(db, db_original=db_user)
