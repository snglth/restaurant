import random
import os

from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from restaurant.schema import Base as schema_base
import restaurant.schema as schema


def init_ingredients(sessionmaker,ingredients_list):
    session = sessionmaker()
    for ingredient in ingredients_list:
        session.add(schema.Ingredient(title=ingredient, unit=schema.Units.piece))
    session.commit()

def make_app():
    app = Flask(__name__)
    app.jinja_env.globals['CAFE_NAME'] = os.environ.get(
        'CAFE_NAME') or "Semyon's Special"
    # engine = create_engine('sqlite:///:memory:', echo=True)
    engine = create_engine('postgresql://postgres:123@172.17.0.2/restaurant',
                           echo=True)
    schema_base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    INGREDIENTS = ['guano', 'feces', 'poop', 'shit', 'fudge']
    init_ingredients(Session, INGREDIENTS)
    return app


# @app.route('/')
# def hello_world():
#     session = Session()
#     ingredients = session.query(schema.Ingredient).all()
#     return render_template('index.html', ingredient=random.choice(ingredients).title)

app = make_app()
