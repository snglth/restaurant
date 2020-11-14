import os

DATABASE_URI = (
    os.environ.get("DATABASE_URI", "postgresql://postgres:123@172.17.0.2/restaurant")
)
CAFE_NAME = (
    os.environ.get("CAFE_NAME", "Semyon's Special")
)
SECRET_KEY = (
    os.environ.get("SECRET_KEY", 'topsecret')
)
