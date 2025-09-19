from flask import request, jsonify, Blueprint
from models import db,  Books

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


@send.route('/ge', methods=['GET'])
def ge():

    book = Books.query.all()
    return jsonify(book)


@send.route('/pu', methods=['PUT'])
def pu():

    data = request.get_json()
    new_author = data.get("author")
    new_id = data.get("new_id")

    if not new_author:
        return jsonify({"message": "new author  required"}), 400
    
    main = Books.query.filter_by(id=new_id).first()

    if main:
        main.author = new_author
        db.session.commit()
        return jsonify({"message": "author updated sucessfully"}), 201

@send.route('/pu_year', methods=['PUT'])
def pu_year():

    data = request.get_json()
    new_year = data.get("new_year")

    if not new_year:
        return jsonify({"message": "new year required"}), 400
    
    main = Books.query.filter_by(year=new_year).first()

    if main:
        main.year = new_year
        db.session.commit()
        return jsonify({"message": "year updated successfully"}), 201


@send.route('/pu_title', methods=['PUT'])
def pu_title():

    data = request.get_json()
    new_title = data.get("new_title")

    if not new_title:
        return jsonify({"message": "new title required"}), 400
    
    main = Books.query.filter_by(title=new_title).first()

    if main:
        main.title = new_title
        db.session.commit()
        return jsonify({"message": "title updated successfully"}), 201
    


@send.route('/dele', methods=['DELETE'])
def dele():

    data = request.get_json()
    author = data.get("author")

    if not author:
        return jsonify({"messaage": "author required"})
    
    delet = Books.query.filter_by(author=author).first()

    if delet:
        db.session.delete(delet)
        db.session.commit()


