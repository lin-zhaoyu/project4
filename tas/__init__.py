from flask import Flask, render_template, redirect, request, session, g, Blueprint, jsonify
import os
import db

def create_app():
    app = Flask(__name__)
    # Configure app key & DB location
    app.config.from_mapping(
        SECRET_KEY = os.urandom(32),
        DATABASE = os.path.join(app.instance_path, db.DB_FILE)
    )
    # Ensure the DB location exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app

app = create_app()

with app.app_context():
    db.init_db()
    d = db.get_db()
    c = d.cursor()


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
