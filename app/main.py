from fastapi import FastAPI

## CORS middle ware lets the specified domains to connect else it will only be able to connect to local host
from fastapi.middleware.cors import CORSMiddleware

# Import Routes to main
from .routers import root, advisor, admin, userRegister, userLogin, getAdvisors, book
## Temp imports 


app = FastAPI()  # creates a new instance of FastAPI


# Routes to include 
app.include_router(root.router)  # Route to root
app.include_router(admin.router)  # Route to admin
app.include_router(advisor.router)  # Route to advisor
app.include_router(userRegister.router)  # Route to advisor
app.include_router(userLogin.router)  # Route to advisor
app.include_router(getAdvisors.router)  # Route to advisor
# app.include_router(book.router)  # Route to advisor