from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from fastapi.responses import HTMLResponse

# use to use router instead of app if used in another file
router = APIRouter(
    prefix="/Admins",
    tags=["Admin"]
)  



@router.get("/", status_code=200, response_class=HTMLResponse)
def root(db:Session = Depends(get_db)):
    admin = db.query(models.Admin).first()
    return f"""
    <html>
        <head>
            <title>Admin</title>
        </head>
        <body>
            <h1>{admin.name}</h1>
            <img src="https://i.ibb.co/gwfjT9z/Nick-Fury.jpg" width="400" height="500">
            <h2>Contact Nick to become an Advisor</h2>
        </body>
    </html>
    """