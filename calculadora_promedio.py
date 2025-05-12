from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calcular_promedio():
    if request.method == 'POST':
        try:
            # Obtener las notas del formulario
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])

            # Calcular el promedio
            promedio = (nota1 + nota2 + nota3) / 3

            # Determinar el resultado
            resultado = "Aprobado" if promedio >= 13.5 else "Desaprobado"
            color_resultado = "green" if promedio >= 13.5 else "red"

            return render_template('index.html', promedio=promedio, resultado=resultado, color_resultado=color_resultado)

        except ValueError:
            error = "Por favor, ingrese valores válidos para las notas."
            return render_template('index.html', error=error)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
