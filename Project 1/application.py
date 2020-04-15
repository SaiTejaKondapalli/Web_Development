import os

# from flask import Flask, session
# from flask_session import Session
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask,render_template,request

app = Flask(__name__)

# # Check for environment variable
# if not os.getenv("DATABASE_URL"):
#     raise RuntimeError("DATABASE_URL is not set")

# # Configure session to use filesystem
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

# # Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/register",methods=["POST"])
def register():
    name1 = request.form['name']
    pswd1 = request.form['pswd']
    pswd2 = request.form['rpswd']
    if pswd1 == pswd2:
        return render_template("register.html", name=name1)
    else:
        wrong = "mismatch"
        return render_template("index.html", name=wrong)

