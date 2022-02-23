#   realizzare un server web che visualizzi l'ora e colori lo sfondo in base all'orario: un colore per la mattina, uno per il pomeriggio ed unno er la notte

from flask import Flask, render_template
app = Flask(__name__)


#  per il tempo
import datetime
# hour = datetime.datetime.now().hour

@app.route('/', methods=['GET'])
def time_sfondocol():
  hour = datetime.datetime.now().hour
  if hour%2 == 0:
    col = "green"
  else:
    col = "red"
  return render_template("per_colore_sfondo.html", colore = col, testo = "hello, World!", ore = hour)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)