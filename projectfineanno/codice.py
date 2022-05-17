
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
quartieri = gpd.read_file("/workspace/Flask/projectfineanno/files/NIL_WM.zip")
alloggiMilano.dropna(inplace = True)



@app.route('/', methods=['GET'])
def HomeP():
    #, nome = hotellombardia.Denominazione struttura == "ALBERGO PAVONE"
  return render_template("homepage.html", quartieri = quartieri.NIL) 

@app.route('/mappapaginainiziale', methods=['GET'])
def mappa():
  m = folium.Map(location=[45.46, 9.20], max_zoom = 18, zoom_start = 12)

  # minimap
  minimap = plugins.MiniMap(toggle_display = True)
  m.add_child(minimap)

  # fullscreem
  plugins.Fullscreen(position="topright").add_to(m)

  # marker
  # for i in range(0,len(alloggiMilano)):
  #  folium.Marker(location=[alloggiMilano.iloc[i]['geo_y'], alloggiMilano.iloc[i]['geo_x']] , popup=alloggiMilano.iloc[i]['DENOMINAZIONE_STRUTTURA']).add_to(m)
  # , tooltip =alloggiMilano.iloc[i]['DENOMINAZIONE_STRUTTURA']
  for (index, row) in alloggiMilano.iterrows():
    
    folium.Marker(location= [row['geo_x'], row['geo_y']], popup=row['DENOMINAZIONE_STRUTTURA']).add_to(m)

  m.save("templates/mappapagin.html")
  return render_template("mappapagin.html")




@app.route('/servizio3', methods=['GET'])
def ricerca():

  quartiere = request.args["quartiere"]
  quartiereUtente = quartieri[quartieri["NIL"] == quartiere]
  Hotelquart = alloggiMilano[alloggiMilano.within(quartiereUtente.geometry.squeeze())]


  return render_template("responseserv3.html", quartieri = quartieri.NIL)

@app.route('/mappaserv3', methods=['GET'])
def mappaserv3():
  m = folium.Map(location=[45.46, 9.20], max_zoom = 18, zoom_start = 12)

  # minimap
  minimap = plugins.MiniMap(toggle_display = True)
  m.add_child(minimap)

  m.save("templates/mapserv3.html")
  return render_template("mapserv3.html")


  # # per far si che nella html non riporti anche l'indice e il suo dtype
  # nome = alloggio["Denominazione struttura"].tolist()
  # cate = alloggio["Categoria"].tolist()
  # ind = alloggio["Indirizzo"].tolist()
  # postael = alloggio["Posta elettronica"].tolist()
  # telefono = alloggio["Telefono"].tolist()

  # , nome = nome[0], cate = cate[0], ind = ind[0], postael = postael[0],
  # telefono = telefono[0]

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)