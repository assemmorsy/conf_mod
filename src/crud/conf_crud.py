from sqlalchemy.orm import Session
from depen.models import Conferance
from depen.tools import clearPunc
from schemas.conf_schemas import ConfCreateSchema,ConfUpdateSchema

class ConfCRUD():

    def get_conf(self,db:Session,conf_id: int):
        # return object or None
        return db.query(Conferance).filter(Conferance.id == conf_id).first()

    def get_confs(self,db:Session,skip: int = 0, limit: int = 100):
        # return list of objects may be empty
        return db.query(Conferance).offset(skip).limit(limit).all()
    
    def get_conf_by_name(self , db:Session,name:str):
        # return object or None
        return db.query(Conferance).filter(Conferance.name == name).first()
    
    def create_conf(self, db:Session,conf: ConfCreateSchema):
        conf.name = clearPunc(conf.name)
        db_conf = Conferance(
            name= conf.name ,
            start_date = conf.start_date,
            end_date = conf.end_date,
            path = conf.path
            )
        db.add(db_conf)
        db.commit()
        db.refresh(db_conf)
        return db_conf

    def update_conf(self,db:Session,conf_id: int, conf:ConfUpdateSchema):
        db_conf = db.query(Conferance).filter(Conferance.id == conf_id).first()
        if db_conf:
            if conf.name : db_conf.name = conf.name 
            if conf.start_date : db_conf.start_date = conf.start_date,
            if conf.end_date : db_conf.end_date = conf.end_date,
            if conf.path : db_conf.path = conf.path

            db.commit()
            db.refresh(db_conf)
        # return updated object or None -> ( can't find object )
        return db_conf
    
    def delete_conf(self,db:Session, conf_id: int):
        db_conf = db.query(Conferance).filter(Conferance.id == conf_id).first()
        if db_conf:
            db.delete(db_conf)
            db.commit()
            return True
        else : 
            return False
        # return True if deleted or false -> ( can't find object )
        