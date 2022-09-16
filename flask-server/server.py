

from flask import Flask, request
from flask_cors import CORS
from src.database import Database

app = Flask(__name__)
CORS(app, origins=["http://localhost:8080"])
# Members API Route
postgres = Database()

@app.route("/")
def home():
    return  "Home"


@app.route("/post_new_user", methods=['POST'])
def post_new_user():
    response = request.get_json()
    postgres.register_user(response["username"], response["email"], response["password"])

    return "Done", 201

@app.route("/login", methods=['POST'])
def logins():
    response = request.get_json()
    postgres.login_user(response["email"], response["password"])

    return "Done", 201


if __name__ == "__main__":
    app.run(debug=True)
