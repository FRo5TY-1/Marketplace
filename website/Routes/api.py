from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user

api = Blueprint("api", __name__)


@api.route('/')
def home():
    return "<h1>Here will be documentation on api, coming soon! </h1>"


@api.route('/items')
def get_items():
    return "<h1>all the items will be here, coming soon! </h1>"


@api.route('/users')
def get_users():
    return "<h1>all the users will be here, coming soon! </h1>"
