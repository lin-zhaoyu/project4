from flask import Flask, render_template, redirect, request, session, g, Blueprint
import json
import os
import urllib3
import sqlite3
import time
from db import get_db, init_task

bp = Blueprint('auth', __name__)


def isAlphaNum(string):
    """
    returns whether a string is alphanumeric
    """
    for char in string:
        o = ord(char)
        if not ((0x41 <= o <= 0x5A) or (0x61 <= o <= 0x7A) or (0x30 <= o <= 0x39)):
            return False
    return True


# Home page
@bp.route("/")
def index():
    return render_template("home.html", user=session.get('username'))

# Signup function
@bp.route("/signup", methods=['GET', 'POST'])
def signup():
    """
        If method = GET, render page to new username & password
        If method = POST, attempts to sign up user, if successful renders login data
    """
    # Obtaining query from html form
    if request.method == "POST":
        print(request.form['username'] + " - " + request.form['password'])
        # Checking if required values in query exist using key values
        if 'username' in request.form and 'password' in request.form:
            d = get_db()
            c = d.cursor()
            # Obtaining data from database
            c.execute("""SELECT username FROM users WHERE username = ?;""",
                      (request.form['username'],))
            exists = c.fetchone()
            # Checking to see if the username that the person signing up gave has not been made
            if (exists == None):
                username = (request.form['username']).encode('utf-8')
                # Check to see if user follows formatting
                if isAlphaNum(username.decode('utf-8')) == None:
                    d.close()
                    return render_template("login.html", user=session.get('username'), action="/signup", name="Sign Up", error="Username can only contain alphanumeric characters.")
                if str(username.decode('utf-8')[0]).isdigit() == True:
                    d.close()
                    return render_template("login.html", user=session.get('username'), action="/signup", name="Sign Up", error="Username cannot start with a number")
                # Check to see if username is of proper length
                if len(username) < 5 or len(username) > 15:
                    d.close()
                    return render_template("login.html", user=session.get('username'), action="/signup", name="Sign Up", error="Usernames must be between 5 and 15 characters long")
                password = request.form['password']
                # Checking for illegal characters in password
                if ' ' in list(password) or '\\' in list(password):
                    d.close()
                    return render_template("login.html", action="/signup", name="Sign Up", error="Passwords cannot contain spaces or backslashes.")
                password = str(password)
                # Checking to see if password follows proper length
                if len(password) > 7 and len(password) <= 50:
                    c.execute("""INSERT INTO users (username,hash) VALUES (?,?)""",
                              (request.form['username'], password))
                    d.commit()
                    c.execute(
                        """SELECT username FROM users WHERE username = ?;""", (request.form['username'],))
                    exists = c.fetchone()
                    #d.close()
                    if (exists != None):
                        print(request.form['username'])
                        init_task(request.form['username'])
                        d.close()
                        return render_template("login.html", action="/login", name="Login", success="Signed up successfully!")
                    else:
                        return render_template("login.html", action="/signup", name="Sign Up", error="Some error occurred. Please try signing up again.")
                else:
                    d.close()
                    return render_template("login.html", action="/signup", name="Sign Up", error="Password must be between 8 and 50 characters long")
            else:
                d.close()
                return render_template("login.html", action="/signup", name="Sign Up", error="Username already exists")
        else:
            return render_template("login.html", action="/signup", name="Sign Up", error="Some error occurred. Please try signing up again.")
    else:
        return render_template("login.html", action="/signup", name="Sign Up")


@bp.route("/login", methods=['GET', 'POST'])
def login():
    """
        If method = GET, render page to enter login info
        If method = POST, attempts to login user with posted data
    """
    if request.method == "POST":
        if 'username' in session:
            return render_template("home.html", user=session.get('username'), message="Already logged in!")
        if 'username' in request.form and 'password' in request.form:
            d = get_db()
            c = d.cursor()
            c.execute("""SELECT hash FROM users WHERE username = ?;""",
                      (request.form['username'],))
            hashed = c.fetchone()  # [0]
            d.close()
            if (hashed == None):
                return render_template("login.html", name="Login", action="/login", error="Invalid username or password")
            else:
                if hashed[0] == request.form['password']:
                    session['username'] = request.form['username']
                    return redirect('/')
                else:
                    return render_template("login.html", name="Login", action="/login", error="Invalid username or password")
        else:
            return render_template("login.html", name="Login", action="/login", error="An error occurred. Please try logging in again.")
    else:
        return render_template("login.html", action="/login", name="Login")


# Logout function
@bp.route("/logout")
def logout():
    """
        Logouts user
    """
    session.pop('username', default=None)
    return redirect("/")
