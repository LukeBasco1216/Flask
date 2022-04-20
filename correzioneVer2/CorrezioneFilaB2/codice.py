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


regioni = gpd.read_file("/workspace/Flask/correzioneVer2/correzioneFilaA2/files/Reg01012021_g_WGS84.dbf")
province = gpd.read_file("/workspace/Flask/correzioneVer2/correzioneFilaA2/files/ProvCM01012021_g_WGS84.dbf")
ripartizioni = gpd.read_file("/workspace/Flask/correzioneVer2/CorrezioneFilaB2/files/georef-italy-ripartizione-geografica.geojson")

@app.route('/', methods=['GET'])
def HomeP():
    return render_template("home.html")


@app.route('/inserimento', methods=['GET'])
def inserimento():
    return render_template("inserimento.html")

@app.route('/datiinput', methods=['GET'])
def datiinput():
    # prendo il valore
    regioneins = request.args["regione"]
    global regioneWgeom
    # cerco il valore nel dataframe
    regioneWgeom = regioni[regioni.DEN_REG.str.contains(regioneins)]
    # misuro la lunghezza del confine
    Lconfine = regioneWgeom.Shape_Leng
    LconfineKm = Lconfine/1000
    # individuo le province dentro la regione
    provinceinreg = province[province.within(regioneWgeom.geometry.squeeze())]
    return render_template("rispostainserimento.html", confine = LconfineKm, tabella = provinceinreg.sort_values(by ="Shape_Area", ascending = False).to_html())

@app.route('/img.png', methods=['GET'])
def img():
    fig, ax = subplots(figsize(12,8))
    regioneWgeom.to_crs(epsg = 3857).plot(ax=ax, edgecolor = "red", facecolor = "none")
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig.print_png(output))
    return Response(output.getvalue(), mimetype = "image/png")




@app.route('/scelta', methods=['GET'])
def scelta():
    return render_template("sceltarip.html", rip = ripartizioni.rip_name)

@app.route('/sceltaripartizione', methods=['GET'])
def sceltaripartizione():
    rip_scelto = request.args["ripartizione"]
    #
    rip_geom = ripartizioni[ripartizioni.rip_name == rip_scelto]
    reginrip = regioni[regioni.within(rip_geom.geometry.squeeze())]
    return render_template("sceltareg.html", reg = reginrip.DEN_REG.sort_values(by="DEN_REG", ascending = True))

@app.route('/selezionereg', methods=['GET'])
def selezionereg():
    return redirect("/datiinput")



@app.route('/sceltalink', methods=['GET'])
def sceltalink():
    return render_template("sceltalink.html", ripa = ripartizioni.rip_name)

@app.route('/sceltareg', methods=['GET'])
def sceltareg():
    rip_scelto = request.args["ripscelto"]
    ripartizione = ripartizioni[ripartizioni.rip_name == rip_scelto]
    regioniinripa = regioni[regioni.within(ripartizione.geometry.squeeze())]
    return render_template("sceltareg2.html", reg = regioniinripa.DEN_REG)

@app.route('/risposta', methods=['GET'])
def risposta():
    return redirect("/datiinpit")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)