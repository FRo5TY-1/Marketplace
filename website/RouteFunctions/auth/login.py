import re
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user
from werkzeug.security import check_password_hash
from ... import db

from website.models import User


def login():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email.lower()).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('No User With This Email', category='error')

    return render_template("Auth/login.html", user=current_user)
