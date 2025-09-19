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

    hold = []

    for me in book:
    #print(book)
        hold.append({
        "author": me.author,
        "title": me.title,
        "year": me.year
    })

    return jsonify(hold)


@send.route('/pu', methods=['PUT'])
def pu():

    data = request.get_json()
    new_author = data.get("new_author")
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
    new_id = data.get("new_id")

    if not new_year:
        return jsonify({"message": "new year required"}), 400
    
    main = Books.query.filter_by(id=new_id).first()

    if main:
        main.year = new_year
        db.session.commit()
        return jsonify({"message": "year updated successfully"}), 201


@send.route('/pu_title', methods=['PUT'])
def pu_title():

    data = request.get_json()
    new_title = data.get("new_title")
    new_id = data.get("new_id")

    if not new_title:
        return jsonify({"message": "new title required"}), 400
    
    main = Books.query.filter_by(id=new_id).first()

    if main:
        main.title = new_title
        db.session.commit()
        return jsonify({"message": "title updated successfully"}), 201
    


@send.route('/dele', methods=['DELETE'])
def dele():

    data = request.get_json()
    rid_author = data.get("rid_author")

    if not rid_author:
        return jsonify({"messaage": "rid_author required"})
    
    delet = Books.query.filter_by(author=rid_author).first()

    if delet:
        db.session.delete(delet)
        db.session.commit()
        return jsonify({"message": "content deleted successfully"}), 201
    return jsonify({"error": f"No book found with id {rid_author}"}), 404


