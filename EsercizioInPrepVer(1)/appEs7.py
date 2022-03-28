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


comuni = gpd.read_file("/workspace/Flask/EsercizioInPrepVer(1)/files/Com01012021_g_WGS84.zip")
province = gpd.read_file("/workspace/Flask/EsercizioInPrepVer(1)/files/ProvCM01012021_g_WGS84.zip")
regioni = gpd.read_file("/workspace/Flask/EsercizioInPrepVer(1)/files/Reg01012021_g_WGS84.zip")

@app.route('/', methods=['GET'])
def HomeP():
  regioniList = [ item for item in regioni.DEN_REG]
  return render_template("home.html", reg=regioniList)


  @app.route('/home', methods=['GET'])
def HomeRis():
  reg_scelto = request.args["regione"]

  return render_template("home.html", reg=regioniList)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)