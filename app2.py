#   realizzare un server web che visualizzi l'ora e colori lo sfondo in base all'orario: un colore per la mattina, uno per il pomeriggio ed unno er la notte

from flask import Flask, render_template
app = Flask(__name__)

import time
start_time = time.time()

@app.route('/', methods=['GET'])
#def colore_sfondo():
#    return (start_time)
print(start_time)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)