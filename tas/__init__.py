from flask import Flask, render_template, redirect, request, session, g, Blueprint, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import db
import auth

app = Flask(__name__)

db.init_db()

app.register_blueprint(auth.bp)

app.secret_key = 'Add your secret key'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    status = db.Column(db.Boolean)

@app.route("/addGoals", methods = ["POST"])
def addGoals():
    title = request.form.get("title")
    new_todo = Todo(title = title, status = False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("goals"))

@app.route("/updateGoals/<int:todo_id>")
def updateGoals(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    print("initial status " + str(todo.status))
    todo.status = not todo.status
    print("initial status "  + str(todo.status))
    db.session.commit()
    return redirect(url_for("goals"))
@app.route("/deleteGoals/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("goals"))
@app.route("/")
def home():
    return render_template("index.html")

# temp just for testing
@app.route("/tas")
def tas():
    return render_template("tas.html")

@app.route("/goals")
def goals():
    todo_list = Todo.query.all()
    print(todo_list);
    return render_template("goals.html", todo_list = todo_list)

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
    db.create_all()
    new_todo = Todo(title="todo 1", status=False)
    db.session.add(new_todo) 
    db.session.commit()
    app.debug = True
    app.run()
