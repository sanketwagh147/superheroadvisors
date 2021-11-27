from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils, oauth
from ..database import get_db

router = APIRouter(
	prefix="/users/register",
	tags=["Users"]
)  #  use to use router instead of app if used in another file

# register a user

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserRegisterOut)
def register_user(user: schemas.UserRegister, db: Session = Depends(get_db)):

	# Check if user already exist
	user_id = db.query(models.User.id).filter(models.User.email == user.email).first()
	if user_id:
		raise HTTPException(status_code=status.HTTP_409_CONFLICT,
						detail= f"This user with user id:{user_id[0]} already exist please login") 

	# If user does not exists then start user creation process

	# hash the password - user.password using hash function from utils library
	hashed_password = utils.hash(user.password)
	user.password = hashed_password

	# Create access token
	access_token = oauth.create_access_token(data={"email": user.email})

	
	new_user = models.User(**user.dict())  # Unpack the post.dict() and pass this way it can be used to pass multiple arguments
	db.add(new_user)  # Add new users to database
	db.commit()  # Commit added changes else the data is not committed
	db.refresh(new_user) # Retrieve new post 

	#Retrieve the new user id from database
	user_id = db.query(models.User.id).filter(models.User.email == user.email).first()[0]

	response_body = {
						"id":user_id,
						"name": user.name,
						"email": user.email,
						"token": access_token
						}
	return response_body

