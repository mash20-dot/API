from flask import request, jsonify, Flask

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)