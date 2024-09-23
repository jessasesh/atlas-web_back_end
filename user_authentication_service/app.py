#!/usr/bin/env python3
"""
Basic Flask App
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def welcome():
    """
    GET method with message
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users():
    """
    Register User
    """
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        AUTH._db.find_user_by(email=email)
        return jsonify({"message": "email already registered"}), 400
    except NoResultFound:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
