
from typing import List, Optional  # list is used for response to send back list 
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, oauth
from ..database import get_db
from sqlalchemy import func
#prefix sets the root so we can start from the prefix instead mentioning it over and over
# If prefix not give write the entire root
router = APIRouter(

    prefix="/users",
    tags=["Users"]   
)

@router.get("/{id}/advisor", response_model=List[schemas.AdvisorsOut])  # return a list of response ibased on schema model
def get_posts(db:Session = Depends(get_db)): 
# def get_posts(db:Session = Depends(get_db), current_user: int = Depends(oauth.get_current_user)): 
    # posts = db.query(models.Advisor).filter(models.Advisor.title.contains(search)).limit(limit).offset(skip).all()   # to get all of the posts 

    # Joining in SQL Alchemy and getting vote count
    print("____________________________________________________________________________________________________")
    posts = db.query(models.Advisor)  # Specify the columns and aggregate function
    print(posts)
    # To get all posts for loged user

    ret_list = []
    for each in posts:
        # print(each.name)
        temp = {}
        temp["name"] = each.name
        temp["id"] = each.id
        temp["image_url"] = each.image_url
        # print(each.image_url)
        ret_list.append(temp)
    print("____________________________________________________________________________________________________")
    print(ret_list)
    # posts = db.query(models.Advisor).filter(models.Advisor.owner_id == current_user.id).all()   # to get all of the posts 
    print("____________________________________________________________________________________________________")
    return ret_list