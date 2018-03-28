from flask import Flask, render_template, request,redirect
app = Flask(__name__)


@app.route('/')
def index():
 return render_template('entry.html',the_title="CLOCK ANGLE")

@app.route('/results', methods=['GET','POST'])
def get_info():
  godzina = float(request.form['godzina'])
  minuta = float(request.form['minuta'])
  stala = float(5.5)

  kat_minuty = stala * minuta
  kat_godziny = (30 * godzina)
  suma_katow = (kat_minuty - kat_godziny)

  def limit():
    if godzina < 25 and minuta < 60:
      if godzina < 0 and minuta < 0:
        return "nie ma minut i godzin na minusie "
      return normalizacja_kata()
    return "Podano zły zakres czasu!"

  def normalizacja_kata():
    if suma_katow > 0:
      if suma_katow < 0:
        return -suma_katow
      return suma_katow
    if -suma_katow < 180:
      return -suma_katow
    if -suma_katow >= 180:
      return suma_katow +360
    if -suma_katow >= 360:
      return (suma_katow +360) * -1

  def wynik():
    return limit()

  return render_template('results.html', the_title='Wynik:',the_minute=minuta,the_hour=godzina,the_result=wynik())

@app.route('/entry')
def strona_powitalna():
    return render_template("entry.html", the_title='CLOCK ANGLE')
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=False)
