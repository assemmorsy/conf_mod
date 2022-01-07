from typing import List
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from depen.database import SessionLocal
from crud.conf_crud import ConfCRUD
from schemas.conf_schemas import ConfUpdateSchema,ConfCreateSchema,ConfSchema

router = APIRouter()
conf_crud = ConfCRUD()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/confs/{conf_id}", response_model=ConfSchema)
def get_conf_by_id(conf_id: int, db: Session = Depends(get_db)):
    db_conf = conf_crud.get_conf(db,conf_id)
    if db_conf is None:
        raise HTTPException(status_code=404, detail="conf not found")
    return db_conf

@router.get("/confs/", response_model=List[ConfSchema])
def get_confs(skip: int = 0, limit: int = 1000,db: Session = Depends(get_db)):
    confs = conf_crud.get_confs(db,skip=skip, limit=limit)
    return confs

@router.post("/confs/", response_model=ConfSchema)
def create_conf(conf: ConfCreateSchema,db: Session = Depends(get_db)):
    db_conf = conf_crud.get_conf_by_name(db,name=conf.name)
    if db_conf != None:
        raise HTTPException(status_code=400, detail="conf already exist")
    conf = conf_crud.create_conf(db,conf)
    return conf


@router.put("/confs/{conf_id}", response_model=ConfSchema)
def update_conf(conf_id: int, conf:ConfUpdateSchema,db: Session = Depends(get_db)):
    db_conf = conf_crud.update_conf(db,conf_id,conf)
    if db_conf is None:
        raise HTTPException(status_code=404, detail="conf is not founded")
    return db_conf


@router.delete("/confs/{conf_id}")
def delete_conf(conf_id: int,db: Session = Depends(get_db)):
    db_conf = conf_crud.delete_conf(db,conf_id)
    if not db_conf :
        raise HTTPException(status_code=404, detail="conf is not founded")
    else:
        return "deleted"
    
