from flask import Flask, render_template
from calculadora import calcular
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculadora.html', etapas = '', resultados = '')

@app.route('/calcular', methods=['POST']) #aqui o /calcular não endereça uma nova página
def calcular_route():
    return calcular()

if __name__ == "__main__":
    app.run(debug=True)