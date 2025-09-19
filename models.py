from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    author = db.Column(db.String(25), nullable=False)
    year = db.Column(db.Integer)
