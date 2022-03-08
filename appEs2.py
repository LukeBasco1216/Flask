# 1a parte
# realizzare un sito web che permetta la reistrazione degli utenti
# l'utente inserisce il nome, uno username, una password 
# la conferma della password e il sesso.
# se l'informazione sono corrette(tutte le caselle piene) il sito salva
# gli informazioni in una struttura dati opportuna (lista di dizionari)

# 2a parte
# prevedere la possibilita di fare il login inserendo il username e il 
# password, se sono corrette fornire un messaggio di benvenuto diverso
# a seconda del sesso, tipo benvenuto/a


from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def registration():
    return render_template("registration.html")


dati = []

@app.route('/data', methods=['POST'])
def data():
    Name = request.args["Name"]
    Username = request.args["Username"]
    Password = request.args["Password"]
    Conferma = request.args["Conferma"]
    if Name == "" or Username == "" or Password == "" or Conferma == "":
        return render_template("notfillederror.html")
    if Password != Conferma:
        return render_template("incorrectPass.html")
    else:





if __name__ == '__main__':
 app.run(host='0.0.0.0', port=3245, debug=True)



