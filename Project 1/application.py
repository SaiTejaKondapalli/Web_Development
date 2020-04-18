import os
import hashlib
from flask import session
from flask_session import Session
from sqlalchemy import create_engine,desc
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, render_template, request
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

@app.route("/")
@app.route("/register",methods=["GET","POST"])
def register():
    # return render_template("index.html")
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        session["data"] = []
        name = request.form['name']
        email = request.form['email']
        pswd1 = request.form['pswd']
        pswdhash1 = hashlib.md5(pswd1.encode()).hexdigest()
        pswd2 = request.form['rpswd']
        pswdhash2 = hashlib.md5(pswd2.encode()).hexdigest()
        if pswd1 == pswd2:
            try:
                user = User(email=email, name=name, pswd=pswdhash1,timestamp=datetime.now())
                db.add(user)
            except:
                return render_template("index.html", name="Registration unsuccessful")
            db.commit()
            return render_template("register.html", name=name)
        else:
            return render_template("index.html", name="Passwords mismatch please register again")
@app.route("/admin", methods=["GET"])
def admin():
    users = db.query(User).order_by(desc(User.timestamp))
    return render_template("admin.html",users = users)
