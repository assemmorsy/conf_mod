from typing import List
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from depen.database import SessionLocal
from crud.speaker_crud import SpeakerCRUD
from schemas.speaker_schemas import SpeakerCreateSchema,SpeakerSchema,SpeakerUpdateSchema

router = APIRouter()
speaker_crud = SpeakerCRUD()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/speakers/{speaker_id}", response_model=SpeakerSchema)
def get_speaker_by_id(speaker_id: int, db: Session = Depends(get_db)):
    db_speaker = speaker_crud.get_speaker(db,speaker_id)
    if db_speaker is None:
        raise HTTPException(status_code=404, detail="Speaker not found")
    return db_speaker

@router.get("/speakers/", response_model=List[SpeakerSchema])
def get_speakers(skip: int = 0, limit: int = 1000,db: Session = Depends(get_db)):
    speakers = speaker_crud.get_speakers(db,skip=skip, limit=limit)
    return speakers

@router.post("/speakers/", response_model=SpeakerSchema)
def create_speaker(speaker: SpeakerCreateSchema,db: Session = Depends(get_db)):
    db_speaker =speaker_crud.get_speaker_by_name(db,name=speaker.name)
    if db_speaker!= None:
        raise HTTPException(status_code=400, detail="Speaker already registered")
    speaker = speaker_crud.create_speaker(db,speaker)
    return speaker


@router.put("/speakers/{speaker_id}", response_model=SpeakerSchema)
def update_speaker(speaker_id: int, speaker:SpeakerUpdateSchema,db: Session = Depends(get_db)):
    db_speaker = speaker_crud.update_speaker(db,speaker_id,speaker)
    if db_speaker is None:
        raise HTTPException(status_code=404, detail="Speaker is not founded")
    return db_speaker


@router.delete("/speakers/{speaker_id}")
def delete_speaker(speaker_id: int,db: Session = Depends(get_db)):
    db_speaker = speaker_crud.delete_speaker(db,speaker_id)
    if not db_speaker :
        raise HTTPException(status_code=404, detail="Speaker is not founded")
    else:
        return "deleted"
    
