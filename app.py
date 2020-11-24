from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'super secret key'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        return redirect('/')
    return render_template('login.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
