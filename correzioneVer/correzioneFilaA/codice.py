from flask import Flask, render_template, send_file, make_response, url_for, Response, request
app = Flask(__name__)
import pandas as pd

import io
import geopandas as gpd
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

stazioni = pd.read_csv("/workspace/Flask/correzioneVer/correzioneFilaA/file/coordfix_ripetitori_radiofonici_milano_160120_loc_final.csv", sep=";")


@app.route('/', methods=['GET'])
def HomeP():
    return render_template("home.html")

@app.route('/numero', methods=['GET'])
def numero():
    # numero di stazione per ogni municipio
    risultato = stazioni.groupby(stazioni.MUNICIPIO, as_index = False).count().filter(items=["MUNICIPIO", "BOUQUET"]).sort_values(by="BOUQUET", ascending = True)
    return render_template("link1.html", tabella = risultato.to_html())


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)