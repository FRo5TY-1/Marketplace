from enum import unique
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy import event
from sqlalchemy.engine import Engine
from . import db


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nickname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    items = db.relationship(
        'Item', cascade="all, delete", passive_deletes=True)


class Item(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "user.id", ondelete="CASCADE"))
    category = db.Column(db.String(60))
    image = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(120))
    description = db.Column(db.String(500))
    price = db.Column(db.Integer)
    fav = db.relationship(
        'Favourites', cascade="all, delete", passive_deletes=True)


class Favourites(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "user.id"))
    item_id = db.Column(db.Integer, db.ForeignKey(
        "item.id", ondelete="CASCADE"))
