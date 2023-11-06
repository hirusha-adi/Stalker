import sqlite3
import os
from datetime import datetime

db_path = os.path.join(os.getcwd(), 'session', 'database.db')


def db_init():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Create the 'sherlock' table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS sherlock (
            id INTEGER PRIMARY KEY,
            uname INTEGER NOT NULL,
            pname TEXT NOT NULL,
            url TEXT NOT NULL,
            http_status INTEGER NOT NULL,
            response_time TEXT NOT NULL
        )
    ''')

    # Create the 'user' table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY,
            uname TEXT NOT NULL,
            uname_sanitized TEXT NOT NULL,
            added_time DATETIME NOT NULL,
            notes INTEGER NOT NULL
        )
    ''')

    # Add a unique constraint to 'user' table
    cur.execute('''
        CREATE UNIQUE INDEX IF NOT EXISTS user_uname_unique ON user (uname)
    ''')

    # Add a foreign key constraint from 'user' to 'sherlock'
    cur.execute('''
        CREATE TABLE IF NOT EXISTS sherlock (
            id INTEGER PRIMARY KEY,
            uname INTEGER NOT NULL,
            pname TEXT NOT NULL,
            url TEXT NOT NULL,
            http_status INTEGER NOT NULL,
            response_time TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


def add_user(uname, uname_sanitized, notes):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    added_time = datetime.now()
    cur.execute("INSERT INTO user (uname, uname_sanitized, added_time, notes) VALUES (?, ?, ?, ?)",
                (uname, uname_sanitized, added_time, notes))
    conn.commit()
    conn.close()


def add_sherlock(uname, pname, url, http_status, response_time):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("INSERT INTO sherlock (uname, pname, url, http_status, response_time) VALUES (?, ?, ?, ?, ?)",
                (uname, pname, url, http_status, response_time))
    conn.commit()
    conn.close()


def get_user_by_uname(uname):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM user WHERE uname=?", (uname,))
    dat = cur.fetchone()
    return dat


def get_sherlock_item_by_uname(uname):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM sherlock WHERE uname=?", (uname,))
    dat = cur.fetchall()
    return dat
