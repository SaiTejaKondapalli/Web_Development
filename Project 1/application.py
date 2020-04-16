import os
import hashlib
from flask import session
from flask_session import Session
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask,render_template,request

app = Flask(__name__)

# # Check for environment variable
# if not os.getenv("DATABASE_URL"):
#     raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# # Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))

@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        session["data"] = []
        name = request.form['name']
        pswd1 = request.form['pswd']
        pswdhash1 = hashlib.md5(pswd1.encode()).hexdigest()
        pswd2 = request.form['rpswd']
        pswdhash2 = hashlib.md5(pswd2.encode()).hexdigest()
        if pswd1 == pswd2:
            return render_template("register.html", name=name)
        else:
            wrong = "mismatch"
            return render_template("index.html", name=wrong)
@app.route("/register",methods=["GET","POST"])
def register():
    return render_template("register.html")

