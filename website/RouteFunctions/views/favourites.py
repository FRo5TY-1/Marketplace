
from flask import render_template, session
from flask_login import current_user, login_required

from website.models import Favourites, Item, User
from ... import db


@login_required
def favourites():
    favourites_array = db.session.query(Item).join(
        Favourites).filter(Favourites.user_id == current_user.id).all()
    return render_template('Views/favourites.html', user=current_user, favourites=favourites_array)
