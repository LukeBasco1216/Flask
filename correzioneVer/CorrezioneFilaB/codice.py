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

stazioni = pd.read_csv("/workspace/Flask/correzioneVer/correzioneFilaA/file/coordfix_ripetitori_radiofonici_milano_160120_loc_final.csv", sep=";")
stazioni_geo = gpd.read_file("/workspace/Flask/correzioneVer/correzioneFilaA/file/stazioniradio.geojson")
quartieri = gpd.read_file("/workspace/Flask/esercizio6/zip files/ds964_nil_wm (2).zip")


@app.route('/', methods=['GET'])
def HomeP():
    return render_template("home.html")

@app.route('/link1', methods=['GET'])
def link1():
    quartordinati = quartieri.groupby(["NIL"], as_index = False).count().filter(items = ["NIL"]).sort_values(by="NIL", ascending = True)
    listaquartord = [ele for ele in quartordinati.NIL]
    return render_template("quartieri.html", lista = listaquartord)

@app.route('/sceltarad', methods=['GET'])
def sceltarad():
    # prende il quartiere scelto
    quartscelto = request.args["quartiere"]
    # prendo il row del quartiere scelto per la sua geometria
    quart = quartieri[quartieri.NIL == quartscelto]
    # trasformo il crs di quart
    quart2 = quart.to_crs(epsg = 4326)
    # cerco gli stazioni nel quartiere 
    stazinquart = stazioni_geo[stazioni_geo.within(quart2.geometry.squeeze())]
    # prendo solo i nomi degli stazioni
    stazinquart = stazinquart.filter(items = ["BOUQUET"]).sort_values(by="BOUQUET", ascending = True)
    return render_template("elencostaz.html", tabella = stazinquart.to_html())




@app.route('/link2', methods=['GET'])
def link2():
    return render_template("input.html")

@app.route('/input', methods=['GET'])
def inputt():
    # prendo il quartiere inserito
    quart = request.args["quartins"]
    # prendo dal dataframe il quartiere inserito per avere la geometria
    quartiere = quartieri[quartieri.NIL.str.contains(quart)]
    # trasformo la crs (per fare dopo il confronto)
    quart2 = quartiere.to_crs(epsg = 4326)
    # prendo gli stazioni dentro il quartiere
    stazinquart = stazioni_geo[stazioni_geo.within(quart2.geometry.squeeze())]
    # faccio l'immagine
    fig, ax = plt.subplots(figsize = (12,8))

    quart2.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor = "k", linewidth = 4)
    stazinquart.to_crs(epsg=3857).plot(ax=ax, markersize = 6, color='black')
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')



@app.route('/link3', methods=['GET'])
def link3():
    # faccio un groupby per avere il numero di stazioni per ogni municipio
    numstaz = stazioni_geo.groupby(["MUNICIPIO"], as_index = False).count().filter(items = ["MUNICIPIO", "BOUQUET"]).sort_values(by = "BOUQUET", ascending =True)
    # figura
    fig, ax = plt.subplots(figsize = (12,8))

    ax.set_xlabel('MUNICIPIO', fontsize=20)
    ax.set_ylabel('N° stazioni', fontsize=20)

    ax.bar(numstaz.MUNICIPIO, numstaz.BOUQUET, color = "r")
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)