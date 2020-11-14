from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from restaurant.config import DATABASE_URI, CAFE_NAME, SECRET_KEY

db = SQLAlchemy()
bs = Bootstrap()
migrate = Migrate()


def make_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SECRET_KEY'] = SECRET_KEY
    app.jinja_env.globals["CAFE_NAME"] = CAFE_NAME

    bs.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from restaurant.blueprints.ingredients import ingredients
    from restaurant.blueprints.index import index

    app.register_blueprint(ingredients)
    app.register_blueprint(index)

    return app
