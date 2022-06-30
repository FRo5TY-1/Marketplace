

import os
from flask import flash, render_template, request
from flask_login import current_user, login_required

from website.models import Favourites, Item, User
from ... import db, base_dir


@login_required
def profile():
    if request.method == "POST":
        item = request.form["delete"]
        item_obj = db.session.query(Item).filter(Item.id == item).first()
        os.remove(os.path.join(base_dir, f"static/Pictures/{item_obj.image}"))
        db.session.delete(item_obj)

        flash("Successfully Deleted Item", category="success")
    items = Item.query.filter_by(user_id=current_user.id).all()
    return render_template('Views/profile.html', user=current_user, items=items)


def other_profile(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        items = Item.query.filter_by(user_id=user.id).all()
        if current_user.is_authenticated:
            favourites = db.session.query(Item).join(
                Favourites).filter(Favourites.user_id == current_user.id).all()
        else:
            favourites = []
        return render_template('Views/other_profile.html', user=current_user, other_user=user, items=items, favourites=favourites)
    else:
        return "<h1>User Not Found</h1>"
