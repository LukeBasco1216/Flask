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
  return render_template("homepage.html")



# @app.route('/plot', methods=("POST", "GET"))
# def mpl():
#     return render_template('plot.html', PageTitle = "Matplotlib")


# @app.route('/plot.png', methods=['GET'])
# def plot_png():

#     fig, ax = plt.subplots(figsize = (12,8))

#     quartieri_milano.to_crs(epsg=3857).plot(ax=ax, alpha=0.5)
#     contextily.add_basemap(ax=ax)
#     output = io.BytesIO()
#     FigureCanvas(fig).print_png(output)
#     return Response(output.getvalue(), mimetype='image/png')


@app.route('/data', methods=("POST", "GET"))
def data():
  quartiere_inserito = request.args["Quartiere"]

  quart = quartieri_milano[quartieri_milano.NIL == quartiere_inserito]

  fig, ax = plt.subplots(figsize = (12,8))

  quart.to_crs(epsg=3857).plot(ax=ax, alpha=0.5)
  contextily.add_basemap(ax=ax)
  output = io.BytesIO()
  FigureCanvas(fig).print_png(output)
  return Response(output.getvalue(), mimetype='image/png')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)