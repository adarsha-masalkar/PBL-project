from flask import Flask, render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/seeds')
def seeds():
    return render_template('seeds_page.html')


@app.route('/fertilizers')
def fertilizers():
    return render_template('progress.html')


@app.route('/crops')
def crops():
    return render_template('progress.html')


@app.route('/soiltest')
def soiltest():
    return render_template('progress.html')


@app.route('/seeds/cotton')
def seeds_cotton_page():
    return render_template('seeds_templates/cotton_page.html')


@app.route('/seeds/paddy')
def seeds_paddy_page():
    return render_template('seeds_templates/paddy_page.html')


@app.route('/seeds/soybean')
def seeds_soybean_page():
    return render_template('seeds_templates/soybean_page.html')


@app.route('/seeds/tur')
def seeds_tur_page():
    return render_template('seeds_templates/tur_page.html')


@app.route('/seeds/jowar')
def seeds_jowar_page():
    return render_template('seeds_templates/jowar_page.html')


@app.route('/seeds/maize')
def seeds_maize_page():
    return render_template('seeds_templates/maize_page.html')


@app.route('/seeds/wheat')
def seeds_wheat_page():
    return render_template('seeds_templates/wheat_page.html')


@app.route('/seeds/gram')
def seeds_gram_page():
    return render_template('seeds_templates/gram_page.html')


if __name__ == "__main__":
    app.run(debug=True)
