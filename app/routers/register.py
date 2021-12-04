from fastapi import status, HTTPException, Depends, APIRouter
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from .. import models, schemas, utils, oauth
from ..database import get_db



router = APIRouter(
    tags=["Home Page"]
)
# register a user



@router.post("/test", status_code=200, response_class=HTMLResponse)
def test_user(name=str = Form(...)):
    return name

