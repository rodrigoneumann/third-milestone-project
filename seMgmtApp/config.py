import os

class Config:
    MONGO_DBNAME = "seMgmtAppDB"
    MONGO_URI = os.getenv("MONGO_URI")
    SECRECT_KEY = os.getenv("SECRET_KEY")