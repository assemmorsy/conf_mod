from typing import Optional
from pydantic import BaseModel


class SpeakerCreateSchema(BaseModel):
    name: str
    qr_id : Optional[int] = None 
    class Config:
        schema_extra = {
            "example": {
                "name": "PROF. Assem Morsy",
                "qr_id": 5,
            }
        }

class SpeakerSchema(BaseModel):
    id: int
    name: str
    qr_id : Optional[int] = None 
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                'id':10,
                "name": "PROF. Assem Morsy",
                "qr_id": 5,
            }
        }

class SpeakerUpdateSchema(BaseModel):
    name: Optional[str] = None
    qr_id : Optional[int] = None 
    class Config:
        schema_extra = {
            "example": {
                "name": "PROF. Assem Morsy",
                "qr_id": 5,
            }
        }