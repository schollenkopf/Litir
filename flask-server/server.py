

from flask import Flask, request
from src.database import Database

app = Flask(__name__)
# Members API Route
d = Database()

@app.route("/")
def home():
    d.populate()
    r = d.fetch()
    return  r


@app.route("/import_raw_data", methods=['POST'])
def import_raw_data():

    print("done")

    return "Done", 201


if __name__ == "__main__":
    app.run(debug=True)
