from flask import Flask
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

#Luetaan kansiosta application tiedoston views sisältö
from application import views

#Luetaan kansiosta application, alikansiosta polls tiedosto models
from application.polls import models
from application.polls import views

#Luodaan lopulta tarvittavat tietokantataulut
db.create_all()
