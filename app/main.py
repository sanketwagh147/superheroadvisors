from fastapi import FastAPI

## CORS middle ware lets the specified domains to connect else it will only be able to connect to local host
from fastapi.middleware.cors import CORSMiddleware

# Import Routes to main
from .routers import root, advisor, admin, userRegister, userLogin, getAdvisors
## Temp imports 


app = FastAPI()  # creates a new instance of FastAPI

origins = ["*"]

app.add_middleware(
    CORSMiddleware,    # Middleware performs some action in beween connection
    allow_origins=origins,   # the origins we allow the domains whihc can talk to our api
    allow_credentials=True,
    allow_methods=["*"],   # allow specific http methods use * to allow all
    allow_headers=["*"],   # allow specific headers only use * to allow all 
)

# Routes to include 
app.include_router(root.router)  # Route to root
app.include_router(admin.router)  # Route to admin
app.include_router(advisor.router)  # Route to advisor
app.include_router(userRegister.router)  # Route to advisor
app.include_router(userLogin.router)  # Route to advisor
app.include_router(getAdvisors.router)  # Route to advisor