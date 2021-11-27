from typing import List  # list is used for response to send back list 
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from .. import models, schemas
from ..database import get_db



#prefix sets the root so we can start from the prefix instead mentioning it over and over
# If prefix not give write the entire root
router = APIRouter(

    prefix="/users",
    tags=["Users"]   
)

@router.get("/{id}/advisor", response_class=HTMLResponse)  # return a list of response i based on schema model
def get_posts(db:Session = Depends(get_db)): 

    posts = db.query(models.Advisor)  
    print(posts)

    advisor_list = []
    for each in posts:
        temp = {}
        temp["name"] = each.name
        temp["id"] = each.id
        temp["image_url"] = each.image_url
        advisor_list.append(temp)
    # print("----------------------------------------------------------------------------------------------------")
    # print(advisor_list)
    # print("----------------------------------------------------------------------------------------------------")
    return html_string(advisor_list)


def html_string(advisors: list):
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
                            {all_advisors}
                        </body>
                    </html>
                    """
    return base_html