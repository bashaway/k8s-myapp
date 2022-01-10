from typing import Optional
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
import groups.model as model
import groups.schema as schema


def get_groups_count(db: Session,
                     id: Optional[str] = None,
                     name: Optional[str] = None,
                     description: Optional[str] = None,
                    ):

    query_groups = db.query(model.Group)

    if id:
        query_groups = query_groups.filter(model.Group.id.contains(id))

    if name:
        query_groups = query_groups.filter(model.Group.name.contains(name))

    if description:
        query_groups = query_groups.filter(model.Group.description.contains(description))

    return {'count': query_groups.count()}


def get_groups(db: Session,
               skip: int = 0,
               limit: int = 100,
               id: Optional[str] = None,
               name: Optional[str] = None,
               description: Optional[str] = None,
              ):

    query_groups = db.query(model.Group)

    if id:
        query_groups = query_groups.filter(model.Group.id.contains(id))

    if name:
        query_groups = query_groups.filter(model.Group.name.contains(name))

    if description:
        query_groups = query_groups.filter(model.Group.description.contains(description))

    return query_groups.offset(skip).limit(limit).all()


def get_group(db: Session, group_id: int):
    return db.query(model.Group).filter(model.Group.id == group_id).first()




def create_group(db: Session, group: schema.GroupCreate):
    db_group = model.Group(name=group.name, description=group.description)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

def update_group( db: Session, group: schema.GroupCreate, original: model.Group) -> model.Group:
    original.name = group.name
    original.email = group.email
    original.group_id = group.group_id
    db.add(original)
    db.commit()
    db.refresh(original)
    return original

def patch_group( db: Session, group: schema.GroupPatch, original: model.Group) -> model.Group:
    update_data = group.dict(exclude_unset=True)
    for key in update_data:
        setattr(original, key , update_data[key])
    db.add(original)
    db.commit()
    db.refresh(original)
    return original


def delete_group(db: Session, original: model.Group) -> model.Group:
    try:
        db.delete(original)
        db.commit()
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=400, detail=original.model_to_json())

    return original
