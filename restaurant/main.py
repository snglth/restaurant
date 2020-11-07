import random

from flask import Flask, render_template
app = Flask(__name__)

INGREDIENTS = [ 'guano', 'feces', 'poop', 'shit', 'fudge' ]

@app.route('/')
def hello_world():
    return render_template('index.jinja2', ingredient=random.choice(INGREDIENTS))

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
