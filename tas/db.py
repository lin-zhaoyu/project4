from flask import g
import sqlite3

DB_FILE="database.db"

create_users = '''CREATE TABLE IF NOT EXISTS USERS(
                ID INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                hash TEXT,
                userfile TEXT)'''


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DB_FILE)
        g.db.row_factory = sqlite3.Row
    return g.db

def init_db():
    d = get_db()
    c = d.cursor()
    c.execute(create_users)
    d.commit()

def init_task(username):
    d = get_db()
    c = d.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS {} (
                    ID INTEGER PRIMARY KEY,
                    tasktitle TEXT,
                    taskdesc TEXT,
                    datetime TEXT,
                    completion BOOLEAN)'''.format(username))
    d.commit()
