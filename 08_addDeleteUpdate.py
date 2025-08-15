from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='admin/templates', static_folder='admin/static')
app.secret_key = "hello"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

class User(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))

    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/view")
def view():
    return render_template("view.html", values=User.query.all())

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user

        found_user =  User.query.filter_by(name=user).delete()
        for user in found_user:
            user.delete()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = User(user, "")
            db.session.add(usr)
            db.session.commit()

        flash("Logged in successfully")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged in")
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/user", methods=["GET", "POST"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = User.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("email was saved")
        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html", email=email)
    else:
        flash("You are not logged in")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash("You have been logged out", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)