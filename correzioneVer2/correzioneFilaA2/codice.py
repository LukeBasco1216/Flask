from flask import Flask, render_template, send_file, make_response, url_for, Response, request, redirect
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


regione = gpd.read_file("/workspace/Flask/correzioneVer2/correzioneFilaA2/files/Reg01012021_g_WGS84.dbf")
province = gpd.read_file("/workspace/Flask/correzioneVer2/correzioneFilaA2/files/ProvCM01012021_g_WGS84.dbf")
comuni = gpd.read_file("/workspace/Flask/correzioneVer2/correzioneFilaA2/files/Com01012021_g_WGS84.dbf")

@app.route('/', methods=['GET'])
def HomeP():
    return render_template("home.html")

@app.route('/sceltaEs', methods=['GET'])
def sceltaEs():
  esScelto = request.args["esercizio"]
  if esScelto == "Esercizio1":
    return redirect("/Es1")
  elif esScelto == "Eserciozio2":
    return redirect("/Es2")
  else:
    return redirect("/Es3")


@app.route('/Es1', methods=['GET'])
def Es1():
  return render_template("input.html")

@app.route('/inputcomune', methods=['GET'])
def inputcomune():
  # prendo il valore inserito
  comScelto = request.args["comune"]
  # cerco il valore nel geodataframe
  comune = comuni[comuni.COMUNE.str.contains(comScelto)]
  # prendo la sua area
  areacom = comune.area/1000
  # cerco i comuni limitrofi, comuni che si trovano al confine del comune
  comlimitrofi = comuni[comuni.touches(comune.geometry.squeeze())].sort_values(by="COMUNE", ascending = True)
  return render_template("responseinput.html", areacomune = areacom, tabella = comlimitrofi.to_html())

@app.route('/mappa', methods=['GET'])
def mappa():
  comScelto = request.args["comune"]
  
  return render_template("responseinput.html")
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)