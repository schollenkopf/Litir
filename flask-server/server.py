

from flask import Flask, request
from flask_cors import CORS
from src.database import Database, EmailAlreadyExsists, WrongPassword

app = Flask(__name__)
CORS(app, origins=["http://localhost:8080", "http://127.0.0.1:8080"])
# Members API Route
postgres = Database()


@app.route("/")
def home():
    return "Home"


@app.route("/post_new_user", methods=['POST'])
def post_new_user():
    response = request.get_json()
    print("HI", response)
    try:
        postgres.register_user(
            response["username"], response["email"], response["password"])
        return "Done", 201
    except EmailAlreadyExsists:
        return "EmailAlreadyExists", 277


@app.route("/login", methods=['POST'])
def logins():
    response = request.get_json()
    try:
        postgres.login_user(response["email"], response["password"])
    except EmailAlreadyExsists:
        return "PasswordIsWrong", 277
    except WrongPassword:
        return "EmailDoesNotExists", 266

    return "Done", 201


if __name__ == "__main__":
    app.run(debug=True)
