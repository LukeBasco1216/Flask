
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
from folium.plugins import MarkerCluster

# import ipywidgets
# import geocoder
# import geopy
# import numpy as np
# from vega_datasets import data as vds



alloggiMilano = gpd.read_file("/workspace/Flask/projectfineanno/files/ds593_strutture-ricettive-alberghiere-e-extra-alberghier_cg7c-84a9_final_geojson.zip", sep=";")
quartieri = gpd.read_file("/workspace/Flask/projectfineanno/files/NIL_WM.zip")

# alloggiMilano = alloggiMilano[alloggiMilano[['geo_x', 'geo_y']].notna()]
alloggiMilano = alloggiMilano[pd.notnull(alloggiMilano['geo_x'])]



@app.route('/', methods=['GET'])
def HomeP():
    #, nome = hotellombardia.Denominazione struttura == "ALBERGO PAVONE"
  return render_template("homepage.html", quartieri = quartieri.NIL) 

@app.route('/mappapaginainiziale', methods=['GET'])
def mappapaginainiziale():

  
  m = folium.Map(location=[45.46, 9.20], max_zoom = 18, zoom_start = 12)

  # minimap
  minimap = plugins.MiniMap(toggle_display = True)
  m.add_child(minimap)

  # fullscreem
  plugins.Fullscreen(position="topright").add_to(m)


  # marker cluster
  marker_cluster = MarkerCluster().add_to(m)

  # marker
  for i in range(0,len(alloggiMilano)):
    
   folium.Marker(
      location=[alloggiMilano.iloc[i]['geo_x'], alloggiMilano.iloc[i]['geo_y']],
      popup=alloggiMilano.iloc[i]['DENOMINAZIONE_STRUTTURA'],
   ).add_to(marker_cluster)

  m.save("templates/mappapagin.html")
  return render_template("mappapagin.html", )




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





if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)