from flask import Flask, request, jsonify
from calculadora_promedio import calcular_promedio

app = Flask(__name__)

@app.route("/promedio", methods=["POST"])
def promedio():
    datos = request.json.get("numeros", [])
    resultado = calcular_promedio(datos)
    return jsonify({"promedio": resultado})
