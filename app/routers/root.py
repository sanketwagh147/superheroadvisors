from fastapi import APIRouter
from fastapi.responses import HTMLResponse


router = APIRouter(
    tags=["Home Page"]
)


@router.get("/", status_code=200, response_class=HTMLResponse)
def root():
    return """
    <html>
        <head>
            <title>Super Hero Advisor App</title>
        </head>
        <body>
            <h1>Welcome to Super Hero Advisor Web App</h1>
            <img src="https://qph.fs.quoracdn.net/main-qimg-0b253fc4c472fddcd4831f5e02235ba2-lq" alt="alternatetext">
            <h2>Get all the Advice you need to become a Super Hero</h2>
        </body>
    </html>
    """