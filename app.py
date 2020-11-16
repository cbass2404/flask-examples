from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Hello! This is the main page!</h1>"


@app.route('/<name>')
def user(name):
    return f"Hello, {name}. How are you doing?"


if __name__ == "__main__":
    app.run(debug=True)
