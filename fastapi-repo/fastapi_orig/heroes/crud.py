from typing import List, Optional
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import Session, select
import heroes.model as model
import common.model as common_model

# レコード数取得
def get_count(db: Session,
    id: Optional[str] = None,
    name: Optional[str] = None,
    secret_name: Optional[str] = None,
    age: Optional[str] = None,
) -> common_model.Count:

    statement = select(model.heroes)

    if id:
        statement = statement.where(model.heroes.id.contains(id))

    if name:
        statement = statement.where(model.heroes.name.contains(name))

    if secret_name:
        statement = statement.where(model.heroes.secret_name.contains(secret_name))

    if age:
        statement = statement.where(model.heroes.age.contains(age))

    return {'count': len(db.exec(statement).all()) }


# 特定の１レコード取得
def get_hero_by_id(db: Session, id: int):
    return db.exec(select(model.heroes).where(model.heroes.id == id)).first()


# 検索
def get_heroes(db: Session, skip, limit,
    id: Optional[str] = None,
    name: Optional[str] = None,
    secret_name: Optional[str] = None,
    age: Optional[str] = None,
):

    statement = select(model.heroes)

    if id:
        statement = statement.where(model.heroes.id.contains(id))

    if name:
        statement = statement.where(model.heroes.name.contains(name))

    if secret_name:
        statement = statement.where(model.heroes.secret_name.contains(secret_name))

    if age:
        statement = statement.where(model.heroes.age.contains(age))

    heroes = db.exec(statement.offset(skip).limit(limit)).all()

    return heroes

# 新規作成
def create_hero(db: Session, hero: model.heroesCreate) -> model.heroesRead:
    db_hero = model.heroes.from_orm(hero)
    db.add(db_hero)
    db.commit()
    db.refresh(db_hero)
    return db_hero


# 更新（PUTによる全フィールド更新）
def update_hero(db: Session, hero: model.heroesBase, db_original: model.heroesRead) -> model.heroes:
    db_hero = model.heroes.from_orm(hero)
    update_data = db_hero.dict(exclude_unset=True)
    for key in update_data:
        setattr(db_original, key , update_data[key])

    try:
        db.add(db_original)
        db.commit()
        db.refresh(db_original)
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=400, detail="database error")
    finally:
        db.close()

    return db_original


# 更新（Patchによるフィールド更新）
def patch_hero(db: Session, hero: model.heroesPatch, db_original: model.heroesRead) -> model.heroes:
    update_data = hero.dict(exclude_unset=True)
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



# 削除
def delete_hero(db: Session, db_original: model.heroes) -> model.heroes:
    try:
        db.delete(db_original)
        db.commit()
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=400, detail=db_original.model_to_json())
    finally:
        db.close()

    return db_original

