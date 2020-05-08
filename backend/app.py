import os
import dataset

from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__,
            static_folder="../dist/static",
            template_folder="../dist")
# CORS only for local dev
cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})

db = dataset.connect(os.getenv('DATABASE_URL', 'sqlite:///data.db'))
table = db["dummy_data"]


@app.route("/api")
def api():
    return jsonify(list(table.all()))


@app.route("/", defaults={"path": ""})
# allows routing in vuejs
@app.route("/<path:path>")
def index(path):
    return render_template("index.html")
