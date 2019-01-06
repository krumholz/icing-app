import os
from flask import Flask, render_template
from flask_sslify import SSLify
from forms import PostForm

app = Flask(__name__)
sslify = SSLify(app, permanent=True)

SECRET_KEY = os.environ.get('APP_SECRET_KEY')
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/")
@app.route("/home")
def home():
    return render_template('layout.html')

@app.route("/signin")
def signin():
    return render_template('signin.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)
