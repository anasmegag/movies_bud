from flask import Flask, request, jsonify
from config import Config
from users import db
from users.model import Users
from users.controller import add_user, login_user

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/add_user', methods=['GET'])
def route_add_user():
    username = request.args.get('username')
    password = request.args.get('password')

    if not username or not password:
        return jsonify({"error": "Veuillez fournir un username et un password"}), 400

    user_id, message = add_user(username, password)
    if user_id is None:
        return jsonify({"message": message}), 400

    return jsonify({"user_id": user_id, "message": message}), 201

@app.route('/login', methods=['GET'])
def route_login():
    username = request.args.get('username')
    password = request.args.get('password')

    if not username or not password:
        return jsonify({"error": "Veuillez fournir un username et un password"}), 400

    user_id, message = login_user(username, password)
    if user_id is None:
        return jsonify({"message": message}), 401

    return jsonify({"user_id": user_id, "message": message}), 200

if __name__ == '__main__':
    app.run(debug=True)
