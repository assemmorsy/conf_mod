from datetime import date
from typing import Optional
from pydantic import BaseModel

class ConfCreateSchema(BaseModel):
    name: str
    start_date : date
    end_date : date
    path : Optional[str] = None
    class Config:
        schema_extra = {
            "example": {
                "name": "TBRI Annual Conference 2021",
                'start_date' : 'YYYY-MM-DD',
                'end_date' : 'YYYY-MM-DD',
                'path': 'TBRI Annual Conference 2021'
            }
        }

class ConfSchema(BaseModel):
    id: int
    name: str
    start_date : date
    end_date : date
    path : Optional[str] = None
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                'id':1,
                "name": "TBRI Annual Conference 2021",
                'start_date' : 'YYYY-MM-DD',
                'end_date' : 'YYYY-MM-DD',
                'path': 'TBRI Annual Conference 2021'
            }
        }

class ConfUpdateSchema(BaseModel):
    name: Optional[str] = None
    start_date : Optional[date] = None
    end_date : Optional[date] = None
    path : Optional[str] = None
    class Config:
        schema_extra = {
            "example": {
                "name": "TBRI Annual Conference 2021",
                'start_date' : 'YYYY-MM-DD',
                'end_date' : 'YYYY-MM-DD',
                'path': 'TBRI Annual Conference 2021'
            }
        }