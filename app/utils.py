from passlib.context import CryptContext

# use bcrypt scheme
pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')

# creates a hash of password
def hash(password: str):
    return pwd_context.hash(password)

#Compare the password to hash in the database
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)