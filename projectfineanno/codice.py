
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


hotellombardia = pd.read_csv("/workspace/Flask/projectfineanno/files/Regione-Lombardia---Mappa-delle-strutture-ricettive.csv", sep=";", encoding='ISO-8859-1', on_bad_lines='skip')

@app.route('/', methods=['GET'])
def HomeP():
  alberghi = hotellombardia[hotellombardia.Categoria == "Alberghiere"]
  return render_template("homepage.html", tabella = alberghi.to_html())





if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)