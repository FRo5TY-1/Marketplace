from flask import Blueprint
from website.RouteFunctions.views.add_item import add_item
from website.RouteFunctions.views.favourites import favourites

from website.RouteFunctions.views.home import home
from website.RouteFunctions.views.item import item_page
from website.RouteFunctions.views.profile import other_profile, profile

views = Blueprint("views", __name__, template_folder="Templates/Views")


views.add_url_rule('/', view_func=home, methods=["GET", "POST"])
views.add_url_rule('/add-item',
                   view_func=add_item, methods=["GET", "POST"])
views.add_url_rule('/favourites', view_func=favourites,
                   methods=["GET", "POST"])
views.add_url_rule('/profile', view_func=profile, methods=["GET", "POST"])
views.add_url_rule('/profile/<int:user_id>',
                   view_func=other_profile, methods=["GET", "POST"])
views.add_url_rule('/item/<int:item_id>',
                   view_func=item_page, methods=["GET", "POST"])
