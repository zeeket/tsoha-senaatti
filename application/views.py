from flask import render_template
from application import app

class Item:
    def __init__(self, name):
        self.name = name

nimi = "Mikko Meikäläinen"

lista = [2,4,6,8,10,12,14,16]

esineet = []
esineet.append(Item("Eka"))
esineet.append(Item("Testi"))
  
@app.route("/demo")
def content():
    return render_template("demo.html", nimi=nimi, lista=lista, esineet=esineet)

@app.route("/")
def index():
    return render_template("index.html")
