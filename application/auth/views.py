from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, argon2
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form, error = "No such username")
    if not argon2.check_password_hash(user.passwordhash,form.password.data):
        return render_template("auth/loginform.html", form = form, error = "Bad password")

    login_user(user)
    return redirect(url_for("index"))    

@app.route("/auth/register", methods = ["GET"])
def auth_register_form():
        return render_template("auth/registerform.html", form = RegisterForm())

@app.route("/auth/register/", methods=["POST"])
def auth_user_create():
    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/registerform.html", form = form)

    u = User(form.username.data,form.password.data)

    db.session().add(u)
    db.session().commit()
    return redirect(url_for("polls_index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))    
