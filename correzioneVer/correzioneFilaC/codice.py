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


quartieri = gpd.read_file("/workspace/Flask/esercizio6/zip files/ds964_nil_wm (2).zip")
linee = gpd.read_file("/workspace/Flask/correzioneVer/correzioneFilaC/file/tpl_percorsi_shp.zip")
linee["lung_km"] = linee["lung_km"].astype(float)
linee["linea"] = linee["linea"].astype(int)


@app.route('/', methods=['GET'])
def HomeP():
  return render_template("home.html")

@app.route('/homedata', methods=['GET'])
def homedata():
    es = request.args["esercizio"]
    if es == "Esercizio1":
      return redirect("/eser1")
    elif es == "Esercizio2":
      return redirect("/eser2")
    else:
      return redirect("/eser3")

 

@app.route('/eser1', methods=['GET'])
def eser1():
  return render_template("inserimentoval.html")

@app.route('/input', methods=['GET'])
def inputt():
  # prendo i valori inseriti trasformandoli in float cosi funziona anche se mette una virgola(punto)
  val1 = float(request.args["val1"])
  val2 = float(request.args["val2"])
  if val1 < val2:
    #prendo le linee tra la lunghezza inserita ordinandolo dal 1 in poi
    percorsi = linee[(linee.lung_km > val1) & (linee.lung_km < val2)][["linea", "lung_km", "num_ferm" , "mezzo", "percorso", "nome", "tipo_perc"]].sort_values(by= "linea", ascending = True)
    return render_template("elencolinee.html", tabella = percorsi.to_html())
  else:
    # se il primo val è magg del secondo ritorna nella stessa pag eliminando cosa c'era scritto
    return render_template("inserimentoval.html")



@app.route('/eser2', methods=['GET'])
def eser2():
  return render_template("inputquartiere.html")

@app.route('/inputquart', methods=['GET'])
def inputquart():
  # prendo il quartiere inserito
  quartins = request.args["quart"]
  # cerco nel df il quartiere inserito per la sua geometria
  quartiere = quartieri[quartieri.NIL.str.contains(quartins)]
  # cerco nel df le linee che attraversano il quartiere inserito prendendo solo la linea e il nome della linea
  lineeInquart = linee[linee.intersects(quartiere.geometry.squeeze())][["linea", "nome"]].sort_values(by = "linea", ascending = True)
  return render_template("elencolineequart.html", tabella = lineeInquart.to_html())


@app.route('/eser3', methods=['GET'])
def eser3():
  # prendo le linee eliminando i duplicati e ordinandolo dal 1 in poi
  return render_template("sceltanumlinea.html", num = linee["linea"].drop_duplicates().sort_values( ascending = True))

@app.route('/scelta', methods=['GET'])
def scelta():
  # prendo la linea scelta 
  numlinea = request.args["linea"]
  # cerco nel df la linea inserita per la sua geometria
  lineageometria = linee[linee.linea == numlinea]

  # faccio l'immagine
  fig, ax = plt.subplots(figsize = (12,8))

  
  lineageometria.to_crs(epsg=3857).plot(ax=ax, edgecolor="k")
  quartieri.to_crs(epsg=3857).plot(ax=ax, facecolor= "none", edgecolor="red")
  contextily.add_basemap(ax=ax)
  output = io.BytesIO()
  FigureCanvas(fig).print_png(output)
  return Response(output.getvalue(), mimetype='image/png')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)