from flask import Flask, render_template, request
from database.db import check_exists, add_user
from funct import *
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa




app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sait.db"
db.init_app(app)
#TODO Моя задача зкалючается сделать стиль на главной страницы, сделать логотип




class Message(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer)
    from_id = db.Column(db.Integer)
    to_id = db.Column(db.Integer)
    time = db.Column(db.String)
    text = db.Column(db.String)



class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    grade = db.Column(db.Integer)
    secret_key = db.Column(db.Integer)

class Ad_table(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    trader_id = db.Column(db.Integer, sa.ForeignKey(User.uid), nullable=False)
    short_desc = db.Column(db.String)
    full_desc = db.Column(db.String)
    type_ad = db.Column(db.String)
    type_bust = db.Column(db.String)
    type_LBZ = db.Column(db.String)
    server = db.Column(db.String, nullable=False)
    fights_count = db.Column(db.Integer)
    win_rait = db.Column(db.Integer)
    raiting = db.Column(db.Integer)
    wn8 = db.Column(db.Integer)
    count = db.Column(db.Integer)
    price = db.Column(db.Integer)
    is_active = db.Column(db.Integer)


@app.route("/lots/<type_>", methods=["POST","GET"])
def test_page(type_):
    try:
        key = request.args['secret_key']
    except:
        key = None
    # print(key, type(key))
    form_data=request.form.to_dict()
    page = create_page_log(type_)
    data = db.session.query(Ad_table).filter_by(type_ad=type_).all()
    data = get_data(data)
    if form_data['secret_key'] != "":
        user = db.session.query(User).filter_by(secret_key=form_data["secret_key"]).first()
        return render_template("mainpage.html", ad=data, page_type=page, if_form=form_data['secret_key'] != "", user=user)
    elif key:
        pass
    user = {"uid": 0}
    return render_template("mainpage.html", ad=data, page_type=page, if_form=form_data['secret_key'] != "", user=user)


@app.route("/", methods=["POST","GET"])
def main_page():
    page = create_page_log('account')
    data = db.session.query(Ad_table).filter_by(type_ad='account').all()
    data = get_data(data)
    form_data=request.form.to_dict()
    print(form_data)
    if len(form_data)>0:
        if form_data['secret_key'] != "":
            user = db.session.query(User).filter_by(secret_key=form_data["secret_key"]).first()
            print(user.uid)
            return render_template("mainpage.html", ad=data, page_type=page, if_form=len(form_data)>0, user=user)

    user ={"uid": 0}
    return render_template("mainpage.html", ad=data, page_type=page, if_form=False, user=user)

# #
# with app.app_context(): #Создает базу данных
#     db.create_all()

@app.route("/register", methods=["POST", "GET"])
def register_page():
    return render_template("regist.html", is_exist=False, false_psw=False)


@app.route("/user_enter")
def user_enter():
    return render_template("user_enter.html", is_email_corect=False, false_psw=False)


@app.route("/user_enter/check", methods=["POST"])
def user_enter_check():
    data = {"email": request.form["email"],
            "password": request.form["psw"]}

    query = db.session.query(User).filter_by(email=data["email"]).first()
    if query == None:
        return render_template("user_enter.html", is_email_corect=True, false_psw=False)
    elif query.email == data["email"]:
        if query.password == data["password"]:
            return render_template("userpage.html", user=query)
        return render_template("user_enter.html", is_email_corect=False, false_psw=True)

@app.route("/register/add", methods=["POST", "GET"])
def register_page_add():
    data = {"user_name": request.form["user_name"],
            "email": request.form["email"],
            "password": request.form["psw"],
            "psw-repeat": request.form["psw-repeat"]}

    query = db.session.query(User).filter_by(user_name=data["user_name"]).first()
    query2 = db.session.query(User).filter_by(email=data["email"]).first()

    if query != None or query2 != None:
        return render_template("regist.html", is_exist=True, false_psw=False)

    if data["password"] == data["psw-repeat"]:
        secret_key = ""
        for simBoL in data["password"]:
            secret_key += str(ord(simBoL))

        user = User(user_name=data["user_name"],
                    email=data["email"],
                    password=data["password"],
                    grade=0,
                    secret_key=int(secret_key))
        db.session.add(user)
        db.session.commit()
        return render_template("userpage.html", user=user)
    return render_template("regist.html", is_exist=False, false_psw=True)


@app.route("/lot_page/<uid>", methods = ["POST", "GET"])
def lot_page(uid):
    form_data = request.args['secret_key']
    post = db.session.query(Ad_table).filter_by(uid=uid).first()
    user = db.session.query(User).filter_by(secret_key=form_data).first()

    data = {
        "uid": post.uid,
        "short_desc": post.short_desc,
        "full_desc": post.full_desc,
        "type_ad": post.type_ad,
        "type_bust": post.type_bust,
        "type_LBZ": post.type_LBZ,
        "server": post.server,
        "fights_count": post.fights_count,
        "win_rait": post.win_rait,
        "raiting": post.raiting,
        "wn8": post.wn8,
        "count": post.count,
        "price": post.price,
        "trader_id": post.trader_id, }
    page = create_page_log(data["type_ad"])
    print(data)
    messages = []
    if user == None:
        user = {"secret_key": "0"}
        return render_template("lot_page.html", data=data, page=page, messages = messages, secret_key=form_data, user=user, authr = False)
    chats = db.session.query(User).filter_by(chat_id = data["uid"], from_id = user.uid, to_id = data["trader_id"].all()
    if data["trader_id"]
    return render_template("lot_page.html", data=data, page=page, messages = messages, secret_key=form_data, user=user, authr = True)


@app.route("/add_ad", methods=["POST","GET"])
def add_ad_page():
    form_data=request.form.to_dict()
    return render_template("add_ad.html", secret_key=form_data["secret_key"])




@app.route("/add_ad/created", methods=["POST"])
def add_ad_created_page():
    data = request.form
    user = db.session.query(User).filter_by(secret_key=data["secret_key"]).first()
    print(user)
    page = ['bust', 'klan', 'other', 'farm']
    if data['type_ad'] == "bonus_kod":
        post = Ad_table(
            short_desc=data["short_desc"],
            full_desc=data["full_desc"],
            count=data["count"],
            server=data["server"],
            type_ad=data["type_ad"],
            price=data["price"],
            trader_id=user.uid)
    elif data['type_ad'] in page:
        post = Ad_table(
            short_desc=data["short_desc"],
            full_desc=data["full_desc"],
            server=data["server"],
            type_ad=data["type_ad"],
            price=data["price"],
            trader_id=user.uid)
    elif data['type_ad'] == "account":
        post = Ad_table(
            short_desc=data["short_desc"],
            full_desc=data["full_desc"],
            server=data["server"],
            type_ad=data["type_ad"],
            price=data["price"],
            wn8=data["WN8"],
            win_rait=data["win_rait"],
            raiting=data["raiting"],
            fights_count=data["fights_count"],
            trader_id=user.uid)
    elif data['type_ad'] == "lbz":
        post = Ad_table(
            type_LBZ=data["type_LBZ"],
            short_desc=data["short_desc"],
            full_desc=data["full_desc"],
            server=data["server"],
            type_ad=data["type_ad"],
            price=data["price"],
            trader_id=user.uid)

    db.session.add(post)
    db.session.commit()
    return render_template("corect_add_ad.html", secret_key=user.secret_key)
@app.route("/chat", methods=["POST", "GET"])
def chat():
    data = request.form
    user = db.session.query(User).filter_by(secret_key=data["secret_key"]).first()
    return render_template("chat.html", user=user)

@app.route("/user_profile/<uid>", methods=["POST", "GET"])
def user_profile(uid):
    user = db.session.query(User).filter_by(uid=int(uid)).first()

    return render_template("userpage.html", user=user)


app.run(debug=True)
