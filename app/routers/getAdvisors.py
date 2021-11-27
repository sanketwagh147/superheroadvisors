
from typing import List  # list is used for response to send back list 
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, oauth
from ..database import get_db



#prefix sets the root so we can start from the prefix instead mentioning it over and over
# If prefix not give write the entire root
router = APIRouter(

    prefix="/users",
    tags=["Users"]   
)

@router.get("/{id}/advisor", response_model=List[schemas.AdvisorsOut])  # return a list of response i based on schema model
def get_posts(db:Session = Depends(get_db)): 

    posts = db.query(models.Advisor)  
    print(posts)

    ret_list = []
    for each in posts:
        temp = {}
        temp["name"] = each.name
        temp["id"] = each.id
        temp["image_url"] = each.image_url
        ret_list.append(temp)
    return ret_list