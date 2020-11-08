import random
import os

from flask import Flask, render_template
from sqlalchemy import create_engine
from restaurant.schema import Base as schema_base

app = Flask(__name__)
app.jinja_env.globals['CAFE_NAME'] = os.environ.get('CAFE_NAME') or "Semyon's Special"

engine = create_engine('postgresql+pg8000://postgres:123@172.17.0.2/restaurant', echo = True)
schema_base.metadata.create_all(engine)


INGREDIENTS = [ 'guano', 'feces', 'poop', 'shit', 'fudge' ]

@app.route('/')
def hello_world():
    return render_template('index.html', ingredient=random.choice(INGREDIENTS))


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)