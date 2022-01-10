from typing import Optional
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
import users.model as model
import users.schema as schema


def get_users_count(db: Session,
                    id: Optional[str] = None,
                    name: Optional[str] = None,
                    email: Optional[str] = None,
                    group_id: Optional[str] = None,
                   ):

    query_users = db.query(model.User)

    if id:
        query_users = query_users.filter(model.User.id.contains(id))

    if name:
        query_users = query_users.filter(model.User.name.contains(name))

    if email:
        query_users = query_users.filter(model.User.email.contains(email))

    if group_id:
        query_users = query_users.filter(model.User.group_id.contains(group_id))

    return {'count': query_users.count()}


def get_users(db: Session,
              skip: int = 0,
              limit: int = 100,
              id: Optional[str] = None,
              name: Optional[str] = None,
              email: Optional[str] = None,
              group_id: Optional[str] = None,
             ):

    query_users = db.query(model.User)

    if id:
        query_users = query_users.filter(model.User.id.contains(id))

    if name:
        query_users = query_users.filter(model.User.name.contains(name))

    if email:
        query_users = query_users.filter(model.User.email.contains(email))

    if group_id:
        query_users = query_users.filter(model.User.group_id.contains(group_id))

    return query_users.offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(model.User).filter(model.User.id == user_id).first()


def create_user(db: Session, user: schema.UserCreate) -> model.User:
    db_user = model.User(name=user.name, email=user.email, group_id=user.group_id)

    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=400, detail=db_user.model_to_json())
    finally:
        db.close()

    return db_user


def update_user( db: Session, user: schema.UserCreate, db_original: model.User) -> model.User:
    update_data = user.dict(exclude_unset=True)
    for key in update_data:
        setattr(db_original, key , update_data[key])

    try:
        db.add(db_original)
        db.commit()
        db.refresh(db_original)
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=400, detail=db_original.model_to_json())
    finally:
        db.close()

    return db_original


def patch_user( db: Session, user: schema.UserPatch, db_original: model.User) -> model.User:
    update_data = user.dict(exclude_unset=True)
    for key in update_data:
        setattr(db_original, key , update_data[key])

    try:
        db.add(db_original)
        db.commit()
        db.refresh(db_original)
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=400, detail=db_original.model_to_json())
    finally:
        db.close()

    return db_original


def delete_user(db: Session, db_original: model.User) -> model.User:
    try:
        db.delete(db_original)
        db.commit()
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=400, detail=db_original.model_to_json())
    finally:
        db.close()

    return db_original
