#   1. Realizzare un server web che come home page presenti tre immagini della stessa dimensione una di fianco all'altra.
# La prima immagine deve avere a che fare con le previsioni del tempo,
# la seconda deve contenere un libro e la terza deve contenere un calendario.
# Utilizzare un file css per definire la grafica della pagina.


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template("html_per_Flask_esercizio_1.html")



#2. modificare il server precedente per far sì che quando l'utente clicca sulla prima immagine vengano fornite le previsioni 
# del tempo.
# Visto che, comunque, le previsioni dei vari servizi metereologici sono sempre sbagliate,
#il nostro server genera un numero casuale compreso tra 0 e 8: se il numero è minore di 2 la previsione è "pioggia",
# se è compreso tra 3 e 5 la previsione è "nuvoloso", se è maggiore di 5 la previsione è "sole".
# Abbinare ad ogni previsione un'immagine adatta. Utilizzare un css per definire la grafica.
# La route per accedere al serizio deve essere /meteo

import random
num_random = random.randint(0,9)
if num_random <= 2:
  tempo = "piovoso.html"
elif num_random >=3 and num_random <=5:
  tempo = "nuvoloso.html"
else:
  tempo = "soleggiato.html"

@app.route('/meteo', methods=['GET'])
def meteo():
    return render_template(tempo)


#3. modificare il server precedente per far sì che quando l'utente clicca sulla seconda immagine il server web
# risponde con una frase celebre, scelta casualmente da un elenco di 10 frasi
# (per ispirazione  https://www.frasimania.it/frasi-corte/). Utilizzare una struttura dati adatta per contenere
# le frasi e gli autori Il sito deve visualizzare la frase con una certa grafica (a scelta) e anche l'autore
# (da visualizzare con una grafica diversa). Utilizzare un file css per definire la grafica della pagina.
#La route per accedere al serizio deve essere /frasicelebri

frasi = [{"autore": "DR. Suess", "Frase": "Sai che sei innamorato quando non vuoi sddormentarti perché la realtà e migliore dei tuoi sogni"},
{"autore": "Oscar Wilde", "Frase": "Amare sè stessi è l'inizio di una storia d'amore lunga tutta una vita"},
{"autore": "Confucio", "Frase": "Studia il passato se vuoi prevedere il futuro"},
{"autore": "Dr. Seuss", "Frase": "Più leggi, più cose saprai. Più cose impari, in più luoghi andrai"},
{"autore": "Albert Einstein", "Frase": "Non considerare mai lo studio come un dovere, ma come un’invidiabile opportunità"},
{"autore": "Marco Tullio Cicerone", "Frase": "L’autorità di chi insegna è spesso un ostacolo per chi vuole imparare"},
{"autore": "Mahatma Gandhi", "Frase": "Vivi come se dovessi morire domani. Impara come se dovessi vivere per sempre"},
{"autore": "André Gide", "Frase": "Sii fedele a ciò che esiste dentro di te"},
{"autore": "Dr. Seuss", "Frase": "Sii ciò che sei e dì ciò che senti, perché quelli a cui importa non contano e a quelli che contano non importa"},
{"autore": "Oscar Wilde", "Frase": "Chi non pensa a se stesso non pensa affatto"}]


num_random2 = random.randint(0,11)
if num_random2 == 1:
  fr = "Sai che sei innamorato quando non vuoi sddormentarti perché la realtà e migliore dei tuoi sogni"
  for ele in frasi:
    if ele["Frase"] == fr:
      @app.route('/frasicelebri', methods=['GET'])
      def frasicel():
        return render_template("frasicelebri.html", frase = fr, autor = ele["autore"] )
elif num_random2 == 2:
  fr = "Amare sè stessi è l'inizio di una storia d'amore lunga tutta una vita"
  for ele in frasi:
    if ele["Frase"] == fr:
      @app.route('/frasicelebri', methods=['GET'])
      def frasicel():
        return render_template("frasicelebri.html", frase = fr, autor = ele["autore"] )
elif num_random2 == 3:
  fr = "Studia il passato se vuoi prevedere il futuro"
  for ele in frasi:
    if ele["Frase"] == fr:
      @app.route('/frasicelebri', methods=['GET'])
      def frasicel():
        return render_template("frasicelebri.html", frase = fr, autor = ele["autore"] )
elif num_random2 == 4:
  fr = "Più leggi, più cose saprai. Più cose impari, in più luoghi andrai"
  for ele in frasi:
    if ele["Frase"] == fr:
      @app.route('/frasicelebri', methods=['GET'])
      def frasicel():
        return render_template("frasicelebri.html", frase = fr, autor = ele["autore"] )
elif num_random2 == 5:
  fr = "Non considerare mai lo studio come un dovere, ma come un’invidiabile opportunità"
  for ele in frasi:
    if ele["Frase"] == fr:
      @app.route('/frasicelebri', methods=['GET'])
      def frasicel():
        return render_template("frasicelebri.html", frase = fr, autor = ele["autore"] )
elif num_random2 == 6:
  fr = "L’autorità di chi insegna è spesso un ostacolo per chi vuole imparare"
  for ele in frasi:
    if ele["Frase"] == fr:
      @app.route('/frasicelebri', methods=['GET'])
      def frasicel():
        return render_template("frasicelebri.html", frase = fr, autor = ele["autore"] )
elif num_random2 == 7:
  fr = "Vivi come se dovessi morire domani. Impara come se dovessi vivere per sempre"
  for ele in frasi:
    if ele["Frase"] == fr:
      @app.route('/frasicelebri', methods=['GET'])
      def frasicel():
        return render_template("frasicelebri.html", frase = fr, autor = ele["autore"] )
elif num_random2 == 8:
  fr = "Sii fedele a ciò che esiste dentro di te"
  for ele in frasi:
    if ele["Frase"] == fr:
      @app.route('/frasicelebri', methods=['GET'])
      def frasicel():
        return render_template("frasicelebri.html", frase = fr, autor = ele["autore"] )
elif num_random2 == 9:
  fr = "Sii ciò che sei e dì ciò che senti, perché quelli a cui importa non contano e a quelli che contano non importa"
  for ele in frasi:
    if ele["Frase"] == fr:
      @app.route('/frasicelebri', methods=['GET'])
      def frasicel():
        return render_template("frasicelebri.html", frase = fr, autor = ele["autore"] )
elif num_random2 == 10:
  fr = "Chi non pensa a se stesso non pensa affatto"
  for ele in frasi:
    if ele["Frase"] == fr:
      @app.route('/frasicelebri', methods=['GET'])
      def frasicel():
        return render_template("frasicelebri.html", frase = fr, autor = ele["autore"] )



# 4. modificare il server precedente per far sì che quando l'utente clicca sulla terza immagine venga visualizzato il numero di giorni
# che mancano alla fine della scuola. Utilizzare un file css per definire la grafica della pagina.
# La route per accedere al serizio deve essere /quantomanca

import datetime
fine_scuola = datetime.date(2022,6,8) - datetime.date.today()


# trasformare in str
date_str = str(fine_scuola)
new_date_str = date_str.replace(" days, 0:00:00", "")
fraseC = "mancano "+ new_date_str + " per la fina della scuola"


@app.route('/quantomanca', methods=['GET'])
def pollofritto():
    return render_template("countdown.html", phrase = fraseC)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

