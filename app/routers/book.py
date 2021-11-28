from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from ..import schemas, database, models, oauth2
from sqlalchemy.orm import Session

# Create a router instance
router = APIRouter(
    prefix="/user",
    tags=["Booking"]
)

@router.post("/{u_id}/advisor/{a_id}", status_code=200)
def book(book: schemas.Book, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    # If booking done on advisor which do not exist
    booking = db.query(models.Book).filter(models.Book.id == book.post_id).first().all()
    if not booking:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f"Advisor with id: {book.post_id} does not exist")

    # Check if advisor is available
    book_query = db.query(models.book).filter(models.book.post_id == book.post_id, models.book.user_id == current_user.id)
    found_booking = book_query.first()
    if (book.status == 1):
        if found_booking:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, 
                                detail=f"This advisor is not available")
        new_book = models.book(post_id=book.post_id, user_id=current_user.id)
        db.add(new_book)
        db.commit()
        return {"message": "Booking Success"}