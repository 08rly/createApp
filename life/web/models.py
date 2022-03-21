from web import db
#from flask_login import UserMixin

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(20), index=True)
    title = db.Column(db.String(30), index=True)
    body = db.Column(db.String(100), nullable=True, index=True)
    date = db.Column(db.Date)

    def __repr__(self):
        return '<Task {}>'.format(self.title)

"""
class User(UserMixin, db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(12))

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def _repr__(self):
        return '<User {}>'.format(self.username)
"""