from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

from send import send

app = Flask(__name__)

app.config['API_KEYS'] = os.getenv('API_KEYS')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///API_DATA.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    author = db.Column(db.String(25), nullable=False)
    year = db.Column(db.Integer)

app.register_blueprint(send, url_prefix='/send')


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
