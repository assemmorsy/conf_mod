from sqlalchemy.orm import Session
from depen.models import Speaker
from depen.tools import clearPunc
from schemas.speaker_schemas import SpeakerCreateSchema,SpeakerUpdateSchema

class SpeakerCRUD():

    def get_speaker(self,db:Session,speaker_id: int):
        # return object or None
        return db.query(Speaker).filter(Speaker.id == speaker_id).first()

    def get_speakers(self,db:Session,skip: int = 0, limit: int = 1000):
        # return list of objects may be empty
        return db.query(Speaker).offset(skip).limit(limit).all()
    
    def get_speaker_by_name(self , db:Session,name:str):
        # return object or None
        return db.query(Speaker).filter(Speaker.name == name).first()
    
    def create_speaker(self, db:Session,speaker: SpeakerCreateSchema):
        speaker.name = clearPunc(speaker.name)
        db_speaker = Speaker(name= speaker.name ,qr_id = speaker.qr_id)
        db.add(db_speaker)
        db.commit()
        db.refresh(db_speaker)
        return db_speaker

    def update_speaker(self,db:Session,speaker_id: int, speaker:SpeakerUpdateSchema):
        db_speaker = db.query(Speaker).filter(Speaker.id == speaker_id).first()
        if db_speaker:
            if speaker.name  : db_speaker.name = speaker.name
            if speaker.qr_id : db_speaker.qr_id = speaker.qr_id
            db.commit()
            db.refresh(db_speaker)
        # return updated object or None -> ( can't find object )
        return db_speaker
    
    def delete_speaker(self,db:Session, speaker_id: int):
        db_speaker = db.query(Speaker).filter(Speaker.id == speaker_id).first()
        if db_speaker:
            db.delete(db_speaker)
            db.commit()
            return True
        else : 
            return False
        # return True if deleted or false -> ( can't find object )
        