
import re
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user
from werkzeug.security import generate_password_hash
from ... import db

from website.models import User


def register():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    if request.method == "POST":
        email = request.form.get('email')
        nickname = request.form.get('nickname')
        password1 = request.form.get('password')
        password2 = request.form.get('repeat-password')

        if validate_data(nickname, email, password1, password2):
            password = generate_password_hash(password1)
            user = User(nickname=nickname,
                        email=email.lower(), password=password)
            db.session.add(user)
            login_user(user, remember=True)
            flash('Registered Successfully!', category='success')
            return redirect(url_for("auth.login"))
        else:
            return redirect(url_for('auth.register'))
    return render_template('Auth/register.html', user=current_user)


def validate_data(nickname, email, pass1, pass2):
    valid = True
    email_regex = '^[a-z0-9A-Z]+[\._]?[a-z0-9A-Z]+[@]\w+[.]\w{2,3}$'

    if len(nickname) < 3:
        flash('Nickname Must Be At Least 3 Characters', category='error')
        valid = False
    if not re.search(email_regex, email):
        flash('Enter A Valid Email', category='error')
        valid = False
    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email Already Used', category='error')
        valid = False
    if len(pass1) < 3:
        flash('Password Must Be At Least 3 Characters', category='error')
        valid = False
    if pass1 != pass2:
        flash('Passwords Don\'t Match', category='error')
        valid = False
    return valid
