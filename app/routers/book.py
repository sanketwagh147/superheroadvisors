from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from ..import schemas, database, models, oauth
from sqlalchemy.orm import Session
from datetime import datetime
from icecream import ic
# Create a router instance
router = APIRouter(
    prefix="/user",
    tags=["Booking"]
)


@router.post("/{uid}/advisor/{a_id}", status_code=200)
def book(uid: int , a_id: int, db: Session = Depends(database.get_db)):
    ic(uid)
    ic(a_id)
    # Check if user id exist
    user = db.query(models.User).filter(models.User.id == uid).first()  # check if user exist 

    # If user not found the in raise error
    if not user:
        raise HTTPException(status_code=404, detail=f"user with user id:{uid} not found please register first")

    # If user found Check if advisor id exist
    advisor = db.query(models.Advisor).filter(models.Advisor.id == a_id).first()  #query if advisor exist

    if not advisor:
        raise HTTPException(status_code=404, detail=f"Advisor with advisor id:{a_id} not found please check advisors list")

    # If both uid and a_id valid check if advisor status is available
    if advisor.status == True:  # if booking status is True proceed to booking  
        raise HTTPException(status_code=404, detail=f"Advisor with advisor id: {a_id} is not available for booking")

    return [uid, a_id, advisor]
    # # If booking done on advisor which do not exist
    # booking = db.query(models.Book).filter(models.Book.id == book.post_id).first().all()
    # if not booking:
    #     raise HTTPException(status.HTTP_404_NOT_FOUND,
    #                         detail=f"Advisor with id: {book.post_id} does not exist")

    # # Check if advisor is available
    # book_query = db.query(models.book).filter(models.book.post_id == book.post_id, models.book.user_id == current_user.id)
    # found_booking = book_query.first()
    # if (book.status == 1):
    #     if found_booking:
    #         raise HTTPException(status_code=status.HTTP_409_CONFLICT, 
    #                             detail=f"This advisor is not available")
    #     new_book = models.book(post_id=book.post_id, user_id=current_user.id)
    #     db.add(new_book)
    #     db.commit()
    #     return {"message": "Booking Success"}
