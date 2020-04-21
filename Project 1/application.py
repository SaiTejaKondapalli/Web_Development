import os
import hashlib
from flask import session
from flask_session import Session
from sqlalchemy import create_engine,desc
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, render_template, request, redirect,url_for
from Database import User
from datetime import datetime

app = Flask(__name__)

# # Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# # Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db_session = scoped_session(sessionmaker(bind=engine))
db = db_session()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        if session.get('data') is not None:
            return render_template("dashboard.html", name=session.get('data'))
        # return redirect(url_for('login'))
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
@app.route("/register/<int:arg>", methods=["GET", "POST"])
def register(arg=None):
    if request.method == "GET":
        if arg == 1:
            msg = "Not registered user !!! Please register here"
            return render_template("index.html", name = msg)
        return render_template("index.html")
    elif request.method == "POST":
        session["data"] = []
        name = request.form['name']
        session["data"].append(name)
        email = request.form['email']
        session["data"].append(email)
        pswd1 = request.form['pswd']
        pswdhash1 = hashlib.md5(pswd1.encode()).hexdigest()
        session["data"].append(pswdhash1)
        pswd2 = request.form['rpswd']
        pswdhash2 = hashlib.md5(pswd2.encode()).hexdigest()
        if pswdhash1 == pswdhash2:
            try:
                user = User(email=email, name=name, pswd=pswdhash1,timestamp=datetime.now())
                db.add(user)
            except:
                return render_template("index.html", name="Registration unsuccessful")
            db.commit()
            return render_template("login.html", name="Registration success. Please login here!!!")
            # return redirect(url_for('login'))
        else:
            return render_template("index.html", name="Passwords mismatch please register again")
@app.route("/admin", methods=["GET"])
def admin():
    users = db.query(User).order_by(desc(User.timestamp))
    return render_template("admin.html", users=users)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route("/auth", methods=["POST"])
def auth():
    uemail = request.form['email']
    pswd = request.form['pswd']
    pswdhashed = hashlib.md5(pswd.encode()).hexdigest()
    users = db.query(User).get(uemail)
    # print(users.email)
    # print(users.pswd)
    if uemail == "":
        return render_template("index.html", name="")
    if users is not None:
        if((uemail==users.email) and (pswdhashed==users.pswd)):
            # print("inside condition")
            session['data'] = uemail
            return render_template("dashboard.html", name="Successfully logged in "+users.name)
    return redirect(url_for('register',arg=1))