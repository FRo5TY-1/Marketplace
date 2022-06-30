
from flask import Request, flash, redirect, render_template, request
from flask_login import current_user, login_required

from website.models import Favourites, Item, User
from ... import db


def home():
    if request.method == "GET":
        if request.args.get('name'):
            items_array = db.session.query(Item, User).join(
                User).filter(Item.name.like(f"%{request.args.get('name')}%")).all()
        elif request.args.get('cat'):
            items_array = db.session.query(Item, User).join(
                User).filter(
                Item.category==request.args.get('cat')).all()
        else:
            items_array = db.session.query(Item, User).join(
                User).all()
        if current_user.is_authenticated:
            favourites = db.session.query(Item).join(
                Favourites).filter(Favourites.user_id == current_user.id).all()
        else:
            favourites = []
        return render_template('Views/home.html', user=current_user, items=items_array, favourites=favourites)
    elif request.method == "POST":
        add_favourite(request)
        return redirect(request.referrer)


@login_required
def add_favourite(request: Request):
    user = current_user
    item = request.form['item']

    if Favourites.query.filter_by(
            item_id=item).all():
        Favourites.query.filter_by(
            item_id=item).delete()
        flash("Removed Item From Favourites", category="error")
    else:
        favourite = Favourites(user_id=user.id, item_id=item)
        db.session.add(favourite)
        flash("Added Item To Favourites", category="success")
