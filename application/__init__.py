from flask import Flask
from flask_argon2 import Argon2
app = Flask(__name__)

#Tuodaan SQLAlchemy käyttöön
from flask_sqlalchemy import SQLAlchemy
#Käytetään database.db nimistä SQLite-tietokantaa. Kolme vinoviivaa
#kertoo ettö tiedosto sijaitsee tämän sovelluksen tiedostojen kanssa
#samassa paikassa
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
#pyydetään SQLAlchemyä tulostamaan kaikki SQL-kyselyt
app.config["SQLALCHEMY_ECHO"] = True

#Luodaan database-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

#Luodaan argon2-olio, jolla tiivistetään salasanat ennen tallentamista
argon2 = Argon2(app)

#Luetaan kansiosta application tiedoston views sisältö
from application import views

#Luetaan kansiosta application, alikansiosta polls tiedostot models&views
from application.polls import models
from application.polls import views

#Luetaan kansiosta application, alikansiosta auth tiedosto models&views
from application.auth import models
from application.auth import views

# kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

#Luodaan lopulta tarvittavat tietokantataulut
db.create_all()
