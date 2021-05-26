from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

import os

uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
# rest of connection code using the connection string `uri`

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["SQLALCHEMY_DATABASE_URI"] = uri
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///User.sqlite3"

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email, gender, password):
        self.name = name
        self.email = email
        self.gender = gender
        self.password = password


@app.route("/")
def home():
    return redirect(url_for('index'))


@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == 'POST':  # When a user clicks submit button it will come here.
        data = request.form  # request the data from the form in index.html file
        name = data["name"]
        email = data["email"]
        gender = data["Gender"]
        password = data["password"]

        new_data = User(name, email, gender, password)
        db.session.add(new_data)
        db.session.commit()

        user_data = User.query.all()
        #print(user_data)

        #return render_template("index.html" , user_data=user_data)  # passes user_data variable into the index.html file.
    return render_template("index.html")

@app.route("/usersdata")
def usersdata():

    return render_template("usersdata.html" ,  user_data = User.query.all())

if __name__ == '__main__':
    app.run(debug=True, port=1602)