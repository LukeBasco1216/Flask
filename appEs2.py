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

@app.route('/data', methods=['GET'])
def data():
    nm = request.args['Name']
    us = request.args['Username']
    pw = request.args['Password']
    confpw = request.args['Conferma']
    Sex = request.args['Sex']
    if confpw == pw:
        dati.append({'Name': nm, 'Username' : us, 'Password' : pw, 'conferma_password' : confpw, 'sesso': Sex})
        print(dati)
        return render_template("login.html", nm= nm, us = us, pw = pw , confpw=confpw,dati= dati)
    else:
        return '<h1>Errore, password non combacia</h1>'



@app.route('/login', methods=['GET'])
def per_log():
    username_log = request.args["Username"]
    pass_log = request.args["Password"]
    for utente in dati:
        # utente[chiave del dizionario]
        if utente["Username"] == username_log and utente["Password"] == pass_log:
            # controllo se l'utente e m o f per il benvenuto
            if utente["sesso"] == "M":
                return render_template("benvenutoM.html", nome_user = utente["Name"])
            else:
                return render_template("benvenutaF.html", nome_user = utente["Name"])

            return render_template("welcomeEs1.html", nome = username_log)
    return render_template("errore.html")
        



if __name__ == '__main__':
   app.run(host='0.0.0.0', port=3245, debug=True)
