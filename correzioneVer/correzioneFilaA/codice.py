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


@app.route('/selezione', methods=['GET'])
def selezione():
    scelta = request.args["scelta"]
    if scelta == "es1":
            # redirect, invece di usare render_template
        return redirect("/numero")
    elif scelta == "es2":
            # redirect to
        return redirect("/input")
    else:
            # redirect to
        return redirect("/dropdown")


@app.route('/numero', methods=['GET'])
def numero():
    # numero di stazione per ogni municipio
    global risultato
    risultato = stazioni.groupby(stazioni.MUNICIPIO, as_index = False).count().filter(items=["MUNICIPIO", "BOUQUET"]).sort_values(by="BOUQUET", ascending = True)
    return render_template("link1.html", tabella = risultato.to_html())


@app.route('/grafico.png', methods=['GET'])
def grafico():
        # costruzione del grafico ( a barre )

    fig, ax = plt.subplots(figsize = (6,4))

    x = risultato.MUNICIPIO
    y = risultato.BOUQUET

    ax.bar(x, y, color = "#304C89")


        #visualizzazione del grafico
    output = io.BytesIO()
    # stampa l'immagine sul canale della comunicazione
    FigureCanvas(fig).print_png(output)
    # manda come risposta, quello che ce nell'output
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/input', methods=['GET'])
def inputt():
    return render_template("link2.html")


@app.route('/ricerca', methods=['GET'])
def ricerca():
    # predni il quartiere inserito
    quartinserito = request.args["quartiere"]
    # cercare nel dataframe dei quartieri il quartiere inserito
    quartiere = quartieri[quartieri.NIL.str.contains(quartinserito)]
    # cercare gli stazioni all'interno del quartiere inserito
    stazquartiere = stazioni_geo[stazioni_geo.within(quartiere.geometry.squeeze())]

    return render_template("elenco1.html", tabella = stazquartiere.to_html())


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)