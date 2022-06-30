from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from website.RouteFunctions.auth.login import login
from website.RouteFunctions.auth.logout import logout

from website.RouteFunctions.auth.register import register
from ..models import User
from .. import db

auth = Blueprint("auth", __name__)


auth.add_url_rule(rule='/register', view_func=register,
                  methods=["GET", "POST"])
auth.add_url_rule(rule='/login', view_func=login, methods=["GET", "POST"])
auth.add_url_rule(rule='/logout', view_func=logout)
