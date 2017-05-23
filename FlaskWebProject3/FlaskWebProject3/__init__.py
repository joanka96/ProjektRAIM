"""
The flask application package.
"""

from flask import Flask, g
from flask.templating import render_template
import sqlite3

DATABASE = 'database.db'

def get_db():
    with app.app_context():
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect(DATABASE)
        return db

def init_db():
    db = get_db()
    #with app.open_resource('schema.sql', mode='r') as f:
    #    db.cursor().executescript(f.read().decode('utf-8-sig'))
    db.commit()

#@app.cli.command('initdb')
#def initdb_command():
#    """Initializes the database."""
#    init_db()
#    print('Initialized the database.')


app = Flask(__name__)
app.secret_key = "super secret key"
init_db()

import FlaskWebProject3.views

