from sqlalchemy.orm import Session
from depen.models import Hall
from depen.tools import clearPunc
from schemas.hall_schemas import hallCreateSchema,hallUpdateSchema

class hallCRUD():

    def get_halls(self,db:Session,conf_id:int,skip: int = 0, limit: int = 100):
        # return list of objects may be empty
        return db.query(Hall).filter(Hall.conf_id == conf_id).offset(skip).limit(limit).all()
    
    def get_hall(self,db:Session,conf_id:int,hall_id: int):
        # return object or None
        conf_halls = self.get_halls(db,conf_id,0,1000)
        return conf_halls.filter(Hall.id == hall_id).first()

    def get_hall_by_name(self , db:Session,conf_id:int,name:str):
        # return object or None
        conf_halls = self.get_halls(db,conf_id,0,1000)
        return conf_halls.filter(Hall.name == name).first()
    
    def create_hall(self, db:Session,conf_id:int,hall: hallCreateSchema):
        hall.name = clearPunc(hall.name)
        db_hall = Hall(
            name= hall.name ,
            start_date = hall.start_date,
            end_date = hall.end_date,
            path = hall.path,
            conf_id = conf_id
            )
        db.add(db_hall)
        db.commit()
        db.refresh(db_hall)
        return db_hall

    def update_hall(self,db:Session,conf_id:int,hall_id: int, hall:hallUpdateSchema):
        db_hall = self.get_hall(db,conf_id,hall_id)

        if db_hall:
            if hall.name : db_hall.name = hall.name 
            if hall.start_date : db_hall.start_date = hall.start_date
            if hall.end_date : db_hall.end_date = hall.end_date
            if hall.path : db_hall.path = hall.path
            if hall.conf_id : db_hall.conf_id = hall.conf_id
            db.commit()
            db.refresh(db_hall)
        # return updated object or None -> ( can't find object )
        return db_hall
    
    def delete_hall(self,db:Session,conf_id:int,hall_id: int):
        db_hall = self.get_hall(db ,conf_id,hall_id )
        if db_hall:
            db.delete(db_hall)
            db.commit()
            return True
        else : 
            return False
        # return True if deleted or false -> ( can't find object )
        