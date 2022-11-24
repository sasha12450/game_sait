from flask import Flask, render_template, request
from database.db import check_exists,add_user
from funct import *
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa

app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sait.db"
db.init_app(app)




class User(db.Model):
    uid = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable=False)
    grade = db.Column(db.Integer)
class Ad_table(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    trader_id = db.Column(db.Integer,  sa.ForeignKey(User.uid), nullable = False)
    short_desc = db.Column(db.String)
    full_desc = db.Column(db.String)
    type_ad = db.Column(db.String)
    type_bust = db.Column(db.String)
    type_LBZ = db.Column(db.String)
    server = db.Column(db.String, nullable = False)
    fights_count =   db.Column(db.Integer)
    rait = db.Column(db.Integer)
    wn8 = db.Column(db.Integer)
    count =  db.Column(db.Integer)
    price  =  db.Column(db.Integer)
    is_active = db.Column(db.Integer)

@app.route("/")
def main_page():
    return render_template("home.html")

# with app.app_context(): Создает базу данных
#     db.create_all()
#
@app.route("/register")
def register_page():

    return render_template("regist.html", is_exist=False, false_psw = False)

@app.route("/register/add", methods = ["POST"])
def register_page_add():
    data = {"user_name": request.form["user_name"],
            "email": request.form["email"],
            "password": request.form["psw"],
            "psw-repeat": request.form["psw-repeat"]}

    query = db.session.query(User).filter_by(user_name=data["user_name"]).first()
    query2 = db.session.query(User).filter_by(user_name=data["email"]).first()

    try:
        query.user_name
        query2.email
        return render_template("regist.html", is_exist=True, false_psw=False)
    except:

        if data["password"] == data["psw-repeat"]:

            user = User(user_name= data["user_name"],
                        email= data["email"],
                        password= data["password"],
                        grade =0)
            db.session.add(user)
            db.session.commit()
            return render_template("home.html")
        return render_template("regist.html", is_exist=False, false_psw=True)








app.run(debug=True)
