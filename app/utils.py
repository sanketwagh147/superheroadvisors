from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')
# use bcrypt scheme

# creates a has of password
def hash(password: str):
    return pwd_context.hash(password)

#Compare the password to hash in the datbase
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)