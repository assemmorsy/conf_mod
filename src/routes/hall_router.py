from typing import List
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from depen.database import SessionLocal
from crud.hall_crud import hallCRUD
from schemas.hall_schemas import HallCreateSchema,HallSchema,HallUpdateSchema

router = APIRouter()
hall_crud = hallCRUD()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/confs/{conf_id}/halls/{hall_id}", response_model=HallSchema)
def get_hall_by_id(conf_id: int,hall_id:int ,  db: Session = Depends(get_db)):
    db_hall = hall_crud.get_hall(db,conf_id,hall_id)
    if db_hall is None:
        raise HTTPException(status_code=404, detail="hall not found")
    return db_hall

@router.get("/confs/{conf_id}/halls/", response_model=List[HallSchema])
def get_halls(conf_id: int,skip: int = 0, limit: int = 1000,db: Session = Depends(get_db)):
    halls = hall_crud.get_halls(db,conf_id,skip,limit)
    return halls

@router.post("/confs/{conf_id}/halls/",response_model=HallSchema)
def create_hall(hall: HallCreateSchema,db: Session = Depends(get_db)):
    db_hall = hall_crud.get_hall_by_name(db,name=hall.name)
    if db_hall != None:
        raise HTTPException(status_code=400, detail="hall already exist")
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
    
