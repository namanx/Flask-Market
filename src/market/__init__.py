from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'bbc7d19bc0531e1c1805c237'
app.app_context().push()

db = SQLAlchemy(app)

from market import models
from market import routes

