from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '8aa2e62480a55d23b269ba558d10bb4d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# the 3 /// are a relative path from the current file


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

app.config['MAIL_SERVER'] = 'mail.local'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = 'app@mail.local'
app.config['MAIL_PASSWORD'] = 'Password'
mail = Mail(app)

from flaskblog import routes
