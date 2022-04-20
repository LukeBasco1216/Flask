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
    return render_template("home2.html" , tabella = ripartizioni.to_html())

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)