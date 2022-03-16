# si vuole realizzare un sito web per memorizzare le squadre di uno sport a scelta.
# l'utente deve poter inserire il nome della squadra e la data di fondazione e la citta.
# deve inoltre poter effettuare delle ricerche inserendo uno dei valore delle colonne  e ottenendo i dati presenti.
# salvare i dati in un dataframe o lista di dizionari o creare un file csv




from flask import Flask, render_template, request
app = Flask(__name__)
import pandas as pd


@app.route('/', methods=['GET'])
def registration():
  return render_template("1stinterface.html")


@app.route('/inserisci', methods=['GET'])
def inserisci():
  return render_template("inserisci.html")

@app.route('/ricerca', methods=['GET'])
def ricerca():
  return render_template("ricerca1stPart.html")



@app.route('/dati', methods=['GET'])
def dati():
    # inserimento dei dati nel file csv
    # lettura dei dati dal form html 
    squadra = request.args['Squadra']
    anno = request.args['Anno']
    citta = request.args['Citta']
    # lettura dei dati daal file nel dataframe
    df1 = pd.read_csv('/workspace/Flask/esercizio5/templates/dati.csv')
    # aggiungiamo i nuovi dati nel dataframe 
    nuovi_dati = {'Team Name':squadra,'Foundation Date':anno,'city ​​of foundation':citta}
    
    df1 = df1.append(nuovi_dati,ignore_index=True)
    # salviamo il dataframe sul file dati.csv
    df1.to_csv('/workspace/Flask/esercizio5/templates/dati.csv', index=False)
    ####### df1.to_html() prende il df e lo converte in html
    return render_template("1stinterface.html")

@app.route('/dataRad', methods=['GET'])
def dataRad():
    Rad_scelto = request.args["sceltaRad"]
    if Rad_scelto == "Team Name":
        return render_template("ricercaTeamName.html")
    elif Rad_scelto == "Foundation Date":
        return render_template("ricercaDateFoundation.html")
    else:
        return render_template("ricercaCityFoundation.html")



@app.route('/dataTN', methods=['GET'])
def ricTN():
    teamName = request.args["TN"]
    dati = pd.read_csv("/workspace/Flask/esercizio5/templates/dati.csv")
    res = dati[dati.Team_Name == teamName]
    return res.to_html()

@app.route('/dataDF', methods=['GET'])
def ricDF():
    FoundationDate = request.args["DF"]
    dati = pd.read_csv("/workspace/Flask/esercizio5/templates/dati.csv")
    # convert column, if not converted ther will be no result because the values in the csv file are int64's and the pc is searching the value as str
    dati["Foundation_Date"] = dati["Foundation_Date"].astype(str)
    res = dati[dati.Foundation_Date == FoundationDate]
    return res.to_html()

@app.route('/dataCF', methods=['GET'])
def ricCF():
    cityoffoundation = request.args["CF"]
    dati = pd.read_csv("/workspace/Flask/esercizio5/templates/dati.csv")
    res = dati[dati.City_of_foundation == cityoffoundation]
    return res.to_html()





if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)