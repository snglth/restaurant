import os
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from restaurant.schema import Base as schema_base


def make_app():
    app = Flask(__name__)
    app.jinja_env.globals["CAFE_NAME"] = (
        os.environ.get("CAFE_NAME") or "Semyon's Special"
    )
    DB_URL = (
        os.environ.get("DB_URL") or "postgresql://postgres:123@172.17.0.2/restaurant"
    )
    engine = create_engine(DB_URL, echo=True)
    schema_base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    return app


app = make_app()
