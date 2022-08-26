

from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
# Members API Route


@app.route("/")
def home():
    return "Home"


@app.route("/import_raw_data", methods=['POST'])
def import_raw_data():

    print("done")

    return "Done", 201


if __name__ == "__main__":
    app.run(debug=True)
