from fastapi import FastAPI

## CORS middle ware lets the specified domains to connect else it will only be able to connect to local host
from fastapi.middleware.cors import CORSMiddleware

# Import Routes to main
from .routers import root, advisor
## Temp imports 


app = FastAPI()  # creates a new instance of FastAPI


# Routes to include 
app.include_router(root.router)  # Route to root
app.include_router(advisor.router)  # Route to advisor
