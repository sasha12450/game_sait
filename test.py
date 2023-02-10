from flask import Flask, render_template, request
from database.db import check_exists, add_user
from funct import *
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa




app = Flask(__name__)
@app.route("/")
def page():
    return render_template("test.html")

@app.route("/add", methods= ["POST", "GET"])
def page2():
    data = request.args['key']
    return data

app.run()