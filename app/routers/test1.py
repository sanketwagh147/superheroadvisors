from fastapi import status, HTTPException, Depends, APIRouter
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from .. import models, schemas, utils, oauth
from ..database import get_db



router = APIRouter(
    tags=["Home Page"]
)
# register a user



@router.get("/users/register", status_code=200, response_class=HTMLResponse)
def register_user():

    # HTML response file
    fname = r"F:\superheroadvisors\app\html\register.html" 

    with open(fname, encoding = 'utf-8') as html_file:
        register = html_file.read() 
    return register
