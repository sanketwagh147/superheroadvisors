from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

# use to use router instead of app if used in another file
router = APIRouter(
    prefix="/admin/advisor",
    tags=["Advisors"]
)  

@router.post("/", status_code=status.HTTP_201_CREATED , response_model=schemas.AdvisorOut)
def create_advisor(advisor: schemas.AdvisorCreate, db: Session = Depends(get_db)):


    # print(advisor.dict())    
    new_advisor = models.Advisor(**advisor.dict())  # Unpack the post.dict() and pass this way it can be used to pass multiple arguments
    db.add(new_advisor)  # Add new entries to data base
    db.commit()  # Commit added changes else the data is not committed
    db.refresh(new_advisor) # Retrieve new post 
    return new_advisor

# Get all advisors
# @router.get('/{id}', response_model= schemas.UserOut)
# def get_advisor(id: int, db: Session = Depends(get_db)):
#     advisor = db.query(models.User).filter(models.User.id == id ).first()


# # If advisor not presenet raise erro
#     if not advisor:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with id: {id} does not exist")

#     return advisor
