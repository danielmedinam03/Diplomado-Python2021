from flask import Flask
from flask.templating import render_template

app = Flask (__name__)
AS='primer variable insertada'
@app.route("/")
def principal():
    return "Hola a todos"

@app.route("/juegos")
def juegos():
    return "Estas en juegos"

@app.route("/ejercicio")
def  docum():
    return render_template('ejercicioPrueba.html',AS='variable insertada')

if __name__ == '__main__':
    app.run(debug=True)
    
    