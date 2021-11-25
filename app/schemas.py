# Create Response and Request Schemas
from pydantic import BaseModel, EmailStr 
from datetime import datetime
from typing import Optional
from pydantic.types import conint


class AdvisorCreate(BaseModel):
    name : str
    image_url : str 

    class Config:
        orm_mode = True

    
class AdvisorOut(BaseModel):
    name : str # Optional for asignment
    # created_at: datetime  # Optional for asignment
    image_url: str

