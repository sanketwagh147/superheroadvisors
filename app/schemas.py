# Create Response and Request Schemas
from pydantic import BaseModel, EmailStr, AnyUrl
from datetime import datetime
from typing import Optional
from pydantic.types import conint


class AdvisorCreate(BaseModel):
    name : str
    image_url : AnyUrl

    
class AdvisorOut(BaseModel):
    name : str # Optional for asignment
    created_at: datetime  # Optional for asignment

