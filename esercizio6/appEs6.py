# realizziamo un sito web che restituisca la mappa dei quartieri di milano.
# ci deve essere una homepage con un link "quartieri di milano"
# cliccando su questo link si deve visualizzare la mappa e quartieri di milano 

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


quartieri_milano = gpd.read_file("/workspace/Flask/esercizio6/zip files/ds964_nil_wm (2).zip")

@app.route('/', methods=['GET'])
def HomeP():
  quartieri = [ item for item in quartieri_milano.NIL]
  return render_template("homepage.html", quartieri=quartieri)



@app.route('/visualizza', methods=['GET'])
def visualizza():
  fig, ax = plt.subplots(figsize = (12,8))

  quartieri_milano.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor = "k", linewidth = 4)
  contextily.add_basemap(ax=ax)
  output = io.BytesIO()
  FigureCanvas(fig).print_png(output)
  return Response(output.getvalue(), mimetype='image/png')



@app.route('/ricerca', methods=['GET'])
def ricerca():
  return render_template("ricerca.html")


@app.route('/data', methods=("POST", "GET"))
def data():
  quartiere_inserito = request.args["Quartiere"]
  quartieri2 = [ item for item in quartieri_milano.NIL]

  quart = quartieri_milano[quartieri_milano.NIL == quartiere_inserito]
  if quartiere_inserito in quartieri2:

    fig, ax = plt.subplots(figsize = (12,8))

    quart.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor = "k", linewidth = 4)
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
  else:
    return render_template("errore.html")



@app.route('/scelta', methods=['GET'])
def scelta():
  quartieri = quartieri_milano.NIL
  return render_template("scelta.html", quartieri=quartieri)


@app.route('/sceltaRis', methods=['GET'])
def sceltaRis():
  quartiere_inserito = request.args["quartie"]

  quart = quartieri_milano[quartieri_milano.NIL == quartiere_inserito]

  fig, ax = plt.subplots(figsize = (12,8))

  quart.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor = "k", linewidth = 4)
  contextily.add_basemap(ax=ax)
  output = io.BytesIO()
  FigureCanvas(fig).print_png(output)
  return Response(output.getvalue(), mimetype='image/png')




fontanelle = gpd.read_file("/workspace/Flask/esercizio6/zip files/Fontanelle (1).zip")

@app.route('/fontanelle', methods=['GET'])
def fontanelle2():
  quartieri = quartieri_milano.NIL
  return render_template("fontanelle.html", quartieri=quartieri)


@app.route('/fonatanellaRis', methods=['GET'])
def fonatanellaRis():
  return render_template('rispostafonta.html',PageTitle = "Matplotlib")



@app.route('/fonatanellaRis2.png', methods=['GET'])
def fonatanellaRis2():
  quartiere_scelto = request.args["quartie"]

  quart = quartieri_milano[quartieri_milano.NIL == quartiere_scelto]

  fontanelle_compreso = fontanelle[fontanelle.within(quart.unary_union)]

  fig, ax = plt.subplots(figsize = (12,8))

  quart.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor = "k", linewidth = 4)
  fontanelle_compreso.to_crs(epsg=3857).plot(ax=ax)
  contextily.add_basemap(ax=ax)
  output = io.BytesIO()
  FigureCanvas(fig).print_png(output)
  return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)