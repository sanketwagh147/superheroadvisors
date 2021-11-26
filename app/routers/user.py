from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils, oauth
from ..database import get_db

router = APIRouter(
    prefix="/users/register",
    tags=["Users"]
)  # use to use router instead of app if used in another file

@router.post("/", status_code=status.HTTP_201_CREATED)
def register_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    print(user)
    print(type(user))
    #hash the password - user.password using hash function from utils library
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    # token = oauth2.create_access_token()
    
    new_user = models.User(**user.dict())  # Unpack the post.dict() and pass this way it can be used to pass multiple arguments
    db.add(new_user)  # Add new users to database
    db.commit()  # Commit added changes else the data is not committed
    db.refresh(new_user) # Retrieve new post 

    return new_user

# @router.get('/{id}', response_model= schemas.UserLoginOut)
# def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id ).first()

# If user not presenet raise erro
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with id: {id} does not exist")

    return user
