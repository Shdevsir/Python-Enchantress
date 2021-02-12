from flask import Flask
from random import randint
app = Flask(__name__)


@app.route("/")
def your_random():
    random_number = randint(-999, 999)
    return f'Hello, your random number is {random_number}'


@app.route('/<name>')
def hello(name):
    return f'Hello {name}'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
