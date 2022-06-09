from flask import Flask, render_template, redirect, request, session, g, Blueprint, jsonify
import os
import db
import auth

app = Flask(__name__)

init_db()

app.register_blueprint(auth.bp)


@app.route("/")
def home():
    return render_template("index.html")

# temp just for testing
@app.route("/tas")
def tas():
    return render_template("tas.html")

@app.route("/goals")
def goals():
    return render_template("goals.html")

@app.route("/rewards")
def rewards():
    return render_template("rewards.html")
@app.route("/logout")
def logout():
    """
        Logouts user
    """
    session.pop('username', default=None)
    return redirect("/")
if __name__ == "__main__":
    app.debug = True
    app.run()
