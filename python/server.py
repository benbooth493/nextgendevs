from flask import Flask, request
import json

users = [
    {
        "id": 0,
        "name": "Ben",
        "age": 43,
    },
    {
        "id": 1,
        "name": "Cait",
        "age": 23,
    },
    {
        "id": 2,
        "name": "Sofia",
        "age": 24,
    },
]

app = Flask(__name__)


@app.route("/id/<name>", methods=["GET"])
def return_user_id(name):
    for user in users:
        if user["name"] == name:
            return str(user["id"])
    return "error: could not find user", 404


@app.route("/new", methods=["POST"])
def create_user():
    data = request.get_json()
    users.append(json.loads(data))
    return "success", 200


@app.route("/users", methods=["GET"])
def list_users():
    return json.dumps(users)
