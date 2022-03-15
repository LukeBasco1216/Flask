# si vuole realizzare un sito web che permetta di visualizzare alcune informazioni sull'andamento dell'epidemia di covid nel nostro paese
# a partire dai dati presenti nel file e mettete nel file https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/platea-dose-addizionale-booster.csv
# l'utente sceglie la regione da un elenco(menu a tendina), clicca su un bottone e il sito deve visualizzare una tabella contenente le informazioni
# relativa a quella regione
# i dati da inserire dal menu a tendina devono essere caricati automaticamente dalla pag web


from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd 

datiCov = pd.read_csv("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/platea-dose-addizionale-booster.csv")

@app.route('/', methods=['GET'])
def index():
    reg = datiCov['nome_area'].drop_duplicates().to_list()
    return render_template('regioneDAscegliere.html', reg=reg)

@app.route('/answ', methods=['GET'])
def answ():
    regione = request.args['vaccini']
    dfres = datiCov[datiCov['nome_area']== regione]
    return render_template('tab_info_cov19.html', tables=[dfres.to_html()], titles=[''])

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)