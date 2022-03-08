# realizzare un server web che permetta di effettuare il login 
# l'utente inserisce lo username  e la password:
# se lo username è admin e la password è xxx123## il sito ci saluta con un messaggio di benvenuto 
# altrimenti ci da un messaggio di errore 
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def per_log():
    return render_template("login.html")


@app.route('/data', methods=['GET'])
def data():
    utente = request.args["Username"]
    Pass = request.args["Password"]
    if utente == "admin" and Pass == "xxx123##":
        return render_template("welcomeEs1.html", nome = utente)
    else:
        return render_template("errore.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)