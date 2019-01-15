from flask import Flask, render_template
app = Flask(__name__)

class Item:
    def __init__(self, name):
        self.name = name

nimi = "Mikko Meikäläinen"

lista = [2,4,6,8,10,12,14,16]

esineet = []
esineet.append(Item("Eka"))
esineet.append(Item("Testi"))
  
@app.route("/")
def hello():
    return render_template("index.html") 

@app.route("/demo")
def content():
    return render_template("demo.html", nimi=nimi, lista=lista, esineet=esineet)

if __name__ == "__main__":
    app.run(debug=True)
