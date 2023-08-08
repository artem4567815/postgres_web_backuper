from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

class Shedules(db.Model):
    __tablename__ = 'shedules'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    databases = db.Column(db.String(50))
    schedule = db.Column(db.String(50))
    freq = db.Column(db.String(50))
    last_update_time = db.Column(db.DateTime(timezone=True), onupdate=func.now())

class Setings(db.Model):
    __tablename__ = 'settings'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    value = db.Column(db.String(50))
