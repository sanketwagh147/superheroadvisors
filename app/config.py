from pydantic import BaseSettings
# Settings for environment variables
class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_username: str
    database_name: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    
    # set to get details from env file
    class Config:
        env_file= ".env"

settings = Settings()