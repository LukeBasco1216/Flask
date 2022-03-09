# 1a parte
# realizzare un server web che permetta di conoscere capoluoghi di regione..
# l'utente inserisce il nome della regione e il programma o l'applicazione reswtituisce il nome
# del capoluogo della regione.
# caricare i capoluoghi e le regioni in una opportuna struttura dati 

# 2a parte
# modificare poi l'esercizion precedente per permetter all'utente di inserire un capoluogo e di avere 
# la regione in cui si trova, l'utente scieglie se avere la regione o il capoluogo selezionando un radio-button


from flask import Flask, render_template, request
app = Flask(__name__)

capoluoghiRegione = {'Abruzzo': 'L\'Aquila','Basilicata': 'Potenza','Calabria': 'Catanzaro','Campania': 'Napoli',
'Emilia-Romagna': 'Bologna','Friuli-Venezia Giulia': 'Trieste','Lazio': 'Roma','Liguria': 'Genova','Lombardia': 'Milano',
'Marche': 'Ancona','Molise': 'Campobasso','Piemonte': 'Torino','Puglia': 'Bari','Sardegna': 'Cagliari','Sicilia': 'Palermo',
'Toscana': 'Firenze','Trentino-Alto Adige': 'Trento','Umbria': 'Perugia','Valle dAosta': 'Aosta','Veneto': 'Venezia'}



@app.route('/', methods=['GET'])
def registration():
   return render_template("inputReg.html")

   
@app.route('/data', methods=['GET'])
def dati():
    regione = request.args['Regione'] 
    








if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

