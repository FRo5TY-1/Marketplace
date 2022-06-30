
from flask import render_template, session
from flask_login import current_user, login_required

from website.models import Favourites, Item, User
from ... import db


@login_required
def item_page(item_id):
    item = Item.query.get(item_id)
    if item:
        favourites_array = db.session.query(Item).join(
            Favourites).filter(Favourites.user_id == current_user.id).all()
        seller = User.query.get(item.user_id)
        return render_template('Views/item.html', user=current_user, item=item, seller=seller, favourites=favourites_array)
    else:
        return "<h1>Item Not Found<\h1>"
