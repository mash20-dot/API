from flask import request, jsonify, Blueprint
from main import db,  Books

send = Blueprint('send', __name__)

@send.route('/po', methods=['POST'])
def po():

    data = request.get_json()
    author =  data.get("author")
    title = data.get("title")
    year = data.get("year")

    if not author or not title or not year:
        return jsonify({"message": "input information"}), 400
    
    submit = Books(title=title, author=author, year=year)
    db.session.add(submit)
    db.session.commit()
    return jsonify({"message": "Book saved"}), 201


