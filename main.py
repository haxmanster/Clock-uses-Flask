from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('entry.html', the_title="CLOCK ANGLE")


@app.route('/results', methods=['GET', 'POST'])
def get_info():
    godzina = float(request.form['godzina'])
    minuta = float(request.form['minuta'])
    stala = float(5.5)
    kat_minuty = stala * minuta
    kat_godziny = (30 * godzina)
    suma_katow = kat_minuty - kat_godziny

    def limit():
        if godzina > 24:
            return "Nie prawidłowy format czasu. Podaj zakres godzin od 0 do 24"
        if minuta > 60:
            return "Nie prawidłowy format czasu. Podaj zakres minut 0d 0 do 60"
        if godzina < 0:
            return "Nie moża cofnąć sie w czasie !!!"
        if minuta < 0:
            return "Nie można cofnąć się w czasie !!! "
        return powyzej_12()

    def powyzej_12():
        if godzina > 12:
            powyzej = godzina - 12
            suma_katow = (30 * powyzej) - kat_minuty
            if abs(suma_katow) > 180:
                return 360 - abs(suma_katow)
            return abs(suma_katow)
        return ponizej_24()

    def ponizej_24():
        if godzina < 13:
            if abs(suma_katow) > 180:
                return 360 - abs(suma_katow)
            return abs(suma_katow)
        return wynik()

    def wynik():
        return limit()

    return render_template('results.html', the_title='Wynik:', the_minute=minuta, the_hour=godzina, the_result=wynik())


@app.route('/entry')
def strona_powitalna():
    return render_template("entry.html", the_title='CLOCK ANGLE')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=80)
