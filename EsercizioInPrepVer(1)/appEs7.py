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
  df_reg_prov = pd.merge(regioni, province, how="right", on=["COD_REG"])
  provinreg = df_reg_prov[df_reg_prov.DEN_REG == reg_scelto]
  return render_template("homeris.html", province2=provinreg.DEN_UTS)



@app.route('/sceltaprov', methods=['GET'])
def sceltaprov():
  # prende la provincia scelta
  prov_scelto = request.args["province"]

  # unisco i df di prov e com
  df_prov_com = pd.merge(province, comuni, how="right", on=["COD_PROV"])
  
  # cerco la prov scelta nel df per avere i suoi comuni
  com_del_prov = df_prov_com[df_prov_com.DEN_PROV == prov_scelto]

  # faccio un groupby per aver i comuni avendo tutte le colonne ma eliminandole con il filter poi riordinandole da A a Z
  comuni_ascendingTrue = com_del_prov.groupby(com_del_prov.COMUNE, as_index = False).count().filter(items = ["COMUNE"]).sort_values(by="COMUNE", ascending = True)

  # lista dei comuni
  lista_com = [ele for ele in comuni_ascendingTrue.COMUNE]

  return render_template("provrisposta.html", lista_com=lista_com, prov_scelto = prov_scelto)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)