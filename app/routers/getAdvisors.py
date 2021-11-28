from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from .. import models
from ..database import get_db
from ..import oauth


#prefix sets the root so we can start from the prefix instead mentioning it over and over
# If prefix not give write the entire root
router = APIRouter(

    prefix="/users",
    tags=["Users"]   
)

@router.get("/{id}/advisor",status_code=200, response_class=HTMLResponse)  # return a list of response i based on schema model
def get_posts(id: int = Depends(oauth.get_current_user), db:Session = Depends(get_db)): 

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