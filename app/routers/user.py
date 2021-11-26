from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(
    prefix="/users/login",
    tags=["Users"]
)  # use to use router instead of app if used in another file

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    #hash the password - user.password using hash function from utils library
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    new_user = models.User(**user.dict())  # Unpack the post.dict() and pass this way it can be used to pass multiple arguments
    db.add(new_user)  # Add new entries to data base
    db.commit()  # Commit added changes else the data is not committed
    db.refresh(new_user) # Retrieve new post 
    return new_user

@router.get('/{id}', response_model= schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id ).first()


# If user not presenet raise erro
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with id: {id} does not exist")

    return user
