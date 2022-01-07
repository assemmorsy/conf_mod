from datetime import date
from typing import Optional
from pydantic import BaseModel

class HallCreateSchema(BaseModel):
    name: str
    start_date : date
    end_date : date
    path : Optional[str] = None
    class Config:
        schema_extra = {
            "example": {
                "name": "TBRI Main Hall",
                'start_date' : 'YYYY-MM-DD',
                'end_date' : 'YYYY-MM-DD',
                'path': 'TBRI Main Hall'
            }
        }

class HallSchema(BaseModel):
    id: int
    name: str
    start_date : date
    end_date : date
    conf_id : int
    path : Optional[str] = None
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                'id':1,
                "name": "TBRI Main Hall",
                'start_date' : 'YYYY-MM-DD',
                'end_date' : 'YYYY-MM-DD',
                'conf_id':1,
                'path': 'TBRI Main Hall'     
            }
        }

class HallUpdateSchema(BaseModel):
    name: Optional[str] = None
    start_date : Optional[date] = None
    end_date : Optional[date] = None
    conf_id :Optional[int] = None
    path : Optional[str] = None
    class Config:
        schema_extra = {
            "example": {
                "name": "TBRI Main Hall",
                'start_date' : 'YYYY-MM-DD',
                'end_date' : 'YYYY-MM-DD',
                'conf_id':1,
                'path': 'TBRI Main Hall'
            }
        }