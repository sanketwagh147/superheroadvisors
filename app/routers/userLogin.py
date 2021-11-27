from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils, oauth

# tags are important to group in docs
router = APIRouter(
                    prefix="/users/login",
                    tags=['Users']
                    )

# Login first time 
@router.post("/", response_model=schemas.UserLoginOut)
def user_login(user_credentials: schemas.UserLogin= Depends(), db: Session = Depends(database.get_db)):
    print("____________________________________________________________________________________________________")
    # check if user email in database
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()  # username 

    # If user not found the in raise error
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid Credentials")
    
    print("___________________END_____________________________________________________________________________")
    # Verify the user entered password and verify using function created  in utils
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid Credentials")

    # Create a JWT token
    access_token = oauth.create_access_token(data={"user_id": user.id})
    # Return a token
    return {"id": user.id, "token": access_token}