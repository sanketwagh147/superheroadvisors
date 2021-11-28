from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from .. import models
from ..database import get_db
from ..import oauth, schemas
from icecream import ic
ic.configureOutput(includeContext=True)

#prefix sets the root so we can start from the prefix instead mentioning it over and over
# If prefix not give write the entire root
router = APIRouter(

    prefix="/users",
    tags=["Users"]   
)
## For Booking
@router.post("/{id}/advisor/{a_id}",status_code=200, response_class=HTMLResponse)  # return a list of response i based on schema model
def book(book :schemas.Book, db:Session = Depends(get_db), id : int = Depends(oauth.get_current_user_id)): 

    # renaming variables 
    current_user_id = id
    requested_advisor = book.a_id
    user_booking_time = book.booking_time
    # Check if user id exist
    user = db.query(models.User).filter(models.User.id == current_user_id).first()  # check if user exist 

    # If user not found the in raise error
    if not user:
        raise HTTPException(status_code=404, detail=f"user with user id:{current_user_id} not found please register first")

    # If user found Check if advisor id exist
    advisor = db.query(models.Advisor).filter(models.Advisor.id == requested_advisor).first()  #query if advisor exist
    if not advisor:
        raise HTTPException(status_code=404, detail=f"Advisor with advisor id:{requested_advisor} not found please check advisors list")

    # If both uid and a_id valid check if advisor status is available
    if advisor.status == True:  # if booking status is True the requested advisor is already booked by other user 
        raise HTTPException(status_code=404, detail=f"Advisor with advisor id: {requested_advisor} is not available for booking")

    # if requested advisor is available modify availability status in database
    q = db.query(models.Advisor).filter(models.Advisor.id == requested_advisor).update({'status': True})
    # ic(q.name)
    # Enter booking detail in booking table
    new_booking = models.Booking(user_id= current_user_id, advisor_id= requested_advisor, booking_time=user_booking_time)
    db.add(new_booking)
    db.commit()

    return  f"""
                    <html>
                        <head>
                
                            <title>Booking Done</title>
                        </head>
                        <body>
                            <h1> Booking Successfull </h1>
                            <h1>User with user ID: {current_user_id} has booked {advisor.name}</h1>
                        </body>
                    </html>
                    """



# GEt all advisors 
@router.get("/{id}/advisor",status_code=200, response_class=HTMLResponse) 
def get_advisors(id: int = Depends(oauth.get_current_user), db:Session = Depends(get_db)): 

    advisors = db.query(models.Advisor)  
    current_user_id = id.id


    advisor_list = []
    for each in advisors:
        temp = {}
        temp["name"] = each.name
        temp["id"] = each.id
        temp["image_url"] = each.image_url
        advisor_list.append(temp)
    return html_string(advisor_list, current_user_id)


def html_string(advisors: list, current_user_id = int):
    all_advisors =""
    for each_advisor in advisors:
        all_advisors +=f" <h{2}>Advisor ID : {each_advisor['id']}</h{2}> "
        all_advisors +=f" <h{2}>Advisor Name : {each_advisor['name']}</h{2}> "
        all_advisors +=f'''<img src={each_advisor['image_url']} width="400" height="500"">'''

    base_html = f"""
                    <html>
                        <head>
                            <title>Super Hero Advisors</title>
                        </head>
                        <body>
                            <h1> All Advisors List </h1>
                            <h1>Current User ID: {current_user_id}</h1>
                            {all_advisors}
                        </body>
                    </html>
                    """
    return base_html


# Get only booked advisors by specific user
@router.get("/{id}/advisor/booking",status_code=200, response_class=HTMLResponse)  
def book(db:Session = Depends(get_db), id : int = Depends(oauth.get_current_user_id)):
    current_user_id = id

    user_booked_advisor_list = []

    query2 = db.query(models.Advisor, models.Booking).join(models.Booking, models.Booking.advisor_id == models.Advisor.id)

    for each in query2:
        temp = [each[0].name ,each[0].image_url, each[0].id, each[1].booking_time, each[1].id]
        user_booked_advisor_list.append(temp)
    return html_string_2(user_booked_advisor_list, current_user_id)

def html_string_2(user_booked_advisor_list, current_user_id):
    all_advisors =""
    for each_advisor in user_booked_advisor_list:
        all_advisors +=f" <h{2}>Advisor Name: {each_advisor[0]}</h{2}> "
        all_advisors +=f" <h{2}>Advisor Id: {each_advisor[2]}</h{2}> "
        all_advisors +=f" <h{2}>Booking Id: {each_advisor[3]}</h{2}> "
        all_advisors +=f" <h{2}>Booking Time: {each_advisor[4]}</h{2}> "
        all_advisors +=f'''<img src={each_advisor[1]} width="400" height="500"">'''

    base_html = f"""
                    <html>
                        <head>
                            <title>Booked Advisors</title>
                        </head>
                        <body>
                            <h1> All Advisors Booked by  </h1>
                            <h1> User ID: {current_user_id}</h1>
                            {all_advisors}
                        </body>
                    </html>
                    """
    return base_html
