from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Golubtsy with guano served! Yay!'

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
