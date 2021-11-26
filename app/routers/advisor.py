from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from fastapi.responses import HTMLResponse

# use to use router instead of app if used in another file
router = APIRouter(
    prefix="/admin/advisor",
    tags=["Advisors"]
)  

@router.post("/", status_code=status.HTTP_201_CREATED, response_class=HTMLResponse)
def create_advisor(advisor: schemas.AdvisorCreate, db: Session = Depends(get_db)):

    #Check if advisor present
    is_advisor =   db.query(models.Advisor).filter(models.Advisor.name == advisor.name).first()
    # print(is_advisor.name)
    # print(type(is_advisor))
    try:
        if is_advisor.name == advisor.name:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail= """ <html><body><h1>Error: Advisor already Added</h1> </body> </html>""")

    except AttributeError:

        # print(advisor.name)    
        new_advisor = models.Advisor(**advisor.dict())  # Unpack the post.dict() and pass this way it can be used to pass multiple arguments
        db.add(new_advisor)  # Add new entries to data base
        db.commit()  # Commit added changes else the data is not committed
        db.refresh(new_advisor) # Retrieve new post 
        # return  new_advisor
        return f"""
        <html>
            <head>
                <title>Success</title>
            </head>
            <body>
                <h1>{new_advisor.name} was added as an Advisor</h1>
                <img src={new_advisor.image_url} width="400" height="500" />
            </body>
        </html>
        """

# Get all advisors
# @router.get('/{id}', response_model= schemas.UserOut)
# def get_advisor(id: int, db: Session = Depends(get_db)):
#     advisor = db.query(models.User).filter(models.User.id == id ).first()


# # If advisor not presenet raise erro
#     if not advisor:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with id: {id} does not exist")

#     return advisor
