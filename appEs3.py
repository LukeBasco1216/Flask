# 1a parte
# realizzare un server web che permetta di conoscere capoluoghi di regione..
# l'utente inserisce il nome della regione e il programma o l'applicazione restituisce il nome
# del capoluogo della regione.
# caricare i capoluoghi e le regioni in una opportuna struttura dati 

# 2a parte
# modificare poi l'esercizio precedente per permettere all'utente di inserire un capoluogo e di avere 
# la regione in cui si trova, l'utente scieglie se avere la regione o il capoluogo selezionando un radio-button


from flask import Flask, render_template, request
app = Flask(__name__)

capoluoghiRegione = [{"Regione":'Abruzzo', "Capoluogo": 'L\'Aquila'},{"Regione":'Basilicata', "Capoluogo": 'Potenza'},{"Regione":'Calabria', "Capoluogo": 'Catanzaro'},
{"Regione":'Campania',"Capoluogo": 'Napoli'},{"Regione": 'Emilia-Romagna',"Capoluogo": 'Bologna'},{"Regione":'Friuli-Venezia Giulia',"Capoluogo": 'Trieste'},
{"Regione": 'Lazio',"Capoluogo": 'Roma'},{"Regione": 'Liguria',"Capoluogo": 'Genova'},{"Regione": 'Lombardia',"Capoluogo": 'Milano'},{"Regione":'Marche',"Capoluogo":'Ancona'},
{"Regione":'Molise', "Capoluogo":'Campobasso'},{"Regione":'Piemonte', "Capoluogo":'Torino'},{"Regione":'Puglia',"Capoluogo": 'Bari'},
{"Regione":'Sardegna',"Capoluogo": 'Cagliari'},{"Regione":'Sicilia',"Capoluogo": 'Palermo'},{"Regione":'Toscana',"Capoluogo": 'Firenze'},
{"Regione":'Trentino-Alto Adige',"Capoluogo": 'Trento'},{"Regione":'Umbria',"Capoluogo": 'Perugia'},{"Regione":'Valle dAosta',"Capoluogo": 'Aosta'},
{"Regione":'Veneto',"Capoluogo": 'Venezia'}]



@app.route('/', methods=['GET'])
def registration():
  return render_template("allInputsforEs3.html")

   
@app.route('/data', methods=['GET'])
def dati():
  reg_cap = request.args['WhatToInsert'] 
  if reg_cap == "Regione":
    return render_template("inserimentoRegione.html")
  else: 
    return render_template("inserimentoCapoluogo.html")
    #  regione_ins = request.args['Regione'] 
    #  for ele in capoluoghiRegione:
    #    if ele["Regione"] == regione_ins:
    #      return render_template("RegCap.html", reg = ele["Regione"], cap = ele["Capoluogo"])
 

@app.route('/datareg', methods=['GET'])
def regi():
    regione_ins = request.args['regione'] 
    for ele in capoluoghiRegione:
      if ele["Regione"] == regione_ins:
        return render_template("RegCap.html", reg = ele["Regione"], cap = ele["Capoluogo"])
      else:
        return render_template("errore.html")

@app.route('/datacap', methods=['GET'])
def capo():
    capoluogo_ins = request.args['capoluogo'] 
    for ele in capoluoghiRegione:
      if ele["Capoluogo"] == capoluogo_ins:
        return render_template("CapReg.html", reg = ele["Regione"], cap = ele["Capoluogo"])
       else:
        return render_template("errore.html")








if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

