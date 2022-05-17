
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

##
import folium
from folium import plugins
# import ipywidgets
# import geocoder
# import geopy
# import numpy as np
# from vega_datasets import data as vds



alloggiMilano = gpd.read_file("/workspace/Flask/projectfineanno/files/ds593_strutture-ricettive-alberghiere-e-extra-alberghier_cg7c-84a9_final_geojson.zip", sep=";")
quartieri = gpd.read_file(")



@app.route('/', methods=['GET'])
def HomeP():
  alloggionelquart = alloggiMilano[alloggiMilano.within(quartiere.geometryy.squeeze())]
  return render_template("newhomepage.html")#, nome = hotellombardia.Denominazione struttura == "ALBERGO PAVONE"

# @app.route('/', methods=['GET'])
# def HomeP():
#   m = folium.Map(location=[45.5236, -122.6750])
#   m.save("testfolium.html")
#   return m

@app.route('/data', methods=['GET'])
def ricerca():
  # nome = request.args["Name"]
  # alloggio = hotellombardia[hotellombardia["Denominazione struttura"].str.contains(nome)]
  # # per far si che nella html non riporti anche l'indice e il suo dtype
  # nome = alloggio["Denominazione struttura"].tolist()
  # cate = alloggio["Categoria"].tolist()
  # ind = alloggio["Indirizzo"].tolist()
  # postael = alloggio["Posta elettronica"].tolist()
  # telefono = alloggio["Telefono"].tolist()

  # , nome = nome[0], cate = cate[0], ind = ind[0], postael = postael[0],
  # telefono = telefono[0]

  return render_template("homepage.html")



@app.route('/mappa', methods=['GET'])
def mappa():
  m = folium.Map(location=[45.46, 9.20], max_zoom = 18, zoom_start = 12)
  m.save("templates/testfolium.html")
  return render_template("testfolium.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)