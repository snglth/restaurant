import random
import os

from flask import Flask, render_template
app = Flask(__name__)
app.jinja_env.globals['CAFE_NAME'] = os.environ['CAFE_NAME']

INGREDIENTS = [ 'guano', 'feces', 'poop', 'shit', 'fudge' ]

@app.route('/')
def hello_world():
    return render_template('index.html', ingredient=random.choice(INGREDIENTS))
