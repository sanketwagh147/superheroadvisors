from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(
    tags=["Home Page"]
)




@router.get("/", status_code=200, response_class=HTMLResponse)
def root():
    fname = r"F:\superheroadvisors\app\html\index.html"
    with open(fname, 'r', encoding='utf-8') as html_file:
        index = html_file.read()

    return index
