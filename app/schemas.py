# Create Response and Request Schemas
from pydantic import BaseModel, EmailStr 
from datetime import datetime
from typing import Optional

# Advisor Schemas

class AdvisorCreate(BaseModel):
    name : str
    image_url : str 
    # status: bool = False
    
class AdvisorOut(BaseModel):
    pass

# User Schemas
class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserRegisterOut(BaseModel):
    id: int
    name: str    # Optional for assignment
    email: str   # optional 
    token : str

    class Config:  # converts to pydantic model 
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserLoginOut(BaseModel):
    id: int
    token: str
    # token_type: str

class TokenData(BaseModel):
    user_id : int 
    
class AdvisorsOut(BaseModel):
    id: int
    name : str # Optional for assignment
    # created_at: datetime  # Optional for assignment
    image_url: str

    class Config:
        orm_mode = True

class Book(BaseModel):
    a_id: int
    booking_time: datetime = None 