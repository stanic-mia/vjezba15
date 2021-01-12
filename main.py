#DZ - kontakt, moji radovi

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/onama")
def onama():
    return render_template("onama.html")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

@app.route("/mojiradovi")
def mojiradovi():
    return render_template("mojiradovi.html")


if __name__ == "__main__":
    app.run()

