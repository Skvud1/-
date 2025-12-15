from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/oxxxy')
def oxxxy():
    return render_template('oxxxy.html')

@app.route('/face')
def face():
    return render_template('face.html')

@app.route('/slava')
def slava():
    return render_template('slava.html')

@app.route('/glossary')
def glossary():
    return render_template('glossary.html')

@app.route('/about')
def about():
    return render_template('about.html')
    пидр

if __name__ == '__main__':
    app.run(debug=True)
