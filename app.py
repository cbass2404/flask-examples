from flask import Flask, request, render_template, redirect, session
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        session['email'] = 'test'
        return redirect('/')
    return render_template('login.html')


@app.route('/logout')
def logout():
    # session['username'] = request.form.get('username')
    # session['username'].
    # session.pop('username', None)
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.debug = True
    app.run()
