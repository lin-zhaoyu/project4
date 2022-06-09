from flask import g
import sqlite3

DB_FILE="database.db"

create_users = '''CREATE TABLE IF NOT EXISTS USERS(
                ID INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                hash TEXT,
                userfile TEXT)'''


def get_db():
    DATABASE = os.path.join(os.path.dirname(__file__), "database.db")
    db = sqlite3.connect(DATABASE, check_same_thread=False, timeout=10)
    return db
    
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
