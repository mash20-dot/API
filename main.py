from flask import Flask
from models import db, Books
import os

from send import send

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///API_DATA.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


app.register_blueprint(send, url_prefix='/send')


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
