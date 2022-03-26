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




@app.route('/', methods=['GET'])
def HomeP():
  quartieri = [ item for item in quartieri_milano.NIL]
  return render_template("homepage.html", quartieri=quartieri)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)