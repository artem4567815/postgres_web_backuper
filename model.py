from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Region(db.Model):
    __tablename__ = 'regions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    parent_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    parent = db.relationship('Region', remote_side=id, primaryjoin=('Region.parent_id==Region.id'), backref='sub-regions')
    created_at = db.Column(db.DateTime, default=db.func.now())
    deleted_at = db.Column(db.DateTime)