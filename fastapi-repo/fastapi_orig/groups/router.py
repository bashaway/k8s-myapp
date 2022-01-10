from typing import List, Optional
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import MetaData
from db import  get_db, engine
import groups.crud as crud
import groups.schema as schema
import groups.model as model
import common.model as common_model

router = APIRouter()

@router.get("/groups/meta", response_model=List[common_model.Meta])
def get_table_columns(db: Session = Depends(get_db)):
    table_name = 'groups'
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


@router.get("/groups/count", response_model=common_model.Count)
def get_groups_count(
                     id: Optional[str] = None,
                     name: Optional[str] = None,
                     description: Optional[str] = None,
                     db: Session = Depends(get_db),
                    ):

    return crud.get_groups_count(db, id=id, name=name, description=description)


@router.get("/groups/", response_model=List[schema.Group])
def read_groups(skip: int = 0,
                limit: int = 100,
                id: Optional[str] = None,
                name: Optional[str] = None,
                description: Optional[str] = None,
                db: Session = Depends(get_db)
               ):

    return crud.get_groups(db, skip=skip, limit=limit, id=id, name=name, description=description)



@router.get("/groups/{group_id}", response_model=schema.Group)
def read_group(group_id: int, db: Session = Depends(get_db)):
    db_group = crud.get_group(db, group_id=group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return db_group


@router.post("/groups/", response_model=schema.Group)
def create_group(group: schema.GroupCreate, db: Session = Depends(get_db)):
    return crud.create_group(db=db, group=group)


@router.put("/groups/{group_id}", response_model=schema.Group)
def update_group( group_id: int, group: schema.GroupCreate, db: Session = Depends(get_db)):
    db_group = crud.get_group(db, group_id=group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return crud.update_group(db, group, original=db_group)


@router.patch("/groups/{group_id}", response_model=schema.Group)
def patch_group(group_id: int, group: schema.GroupPatch, db: Session = Depends(get_db)):
    db_group = crud.get_group(db, group_id=group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return crud.patch_group(db, group, original=db_group)


@router.delete("/groups/{group_id}", response_model=schema.Group)
def delete_group(group_id: int, db: Session = Depends(get_db)):
    db_group = crud.get_group(db, group_id=group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return crud.delete_group(db, original=db_group)
