from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '8aa2e62480a55d23b269ba558d10bb4d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# the 3 /// are a relative path from the current file

db = SQLAlchemy(app)

from flaskblog import routes