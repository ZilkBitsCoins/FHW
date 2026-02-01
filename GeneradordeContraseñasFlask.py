import flask as fk
from flask import request, redirect, url_for
import random

app = fk.Flask(__name__)

@app.route('/')
def home():
    return '''
        <form action="/generar" method="post">
            Longitud de la contraseña: <input type="number" name="longitud" min="1" max="100" required>
            <input type="submit" value="Generar">
        </form>
    '''
@app.route('/generar', methods=['POST'])
def generar():
    longitud = int(request.form['longitud'])
    return redirect(url_for('generar_contrasena', longitud=longitud))

@app.route('/generar/<int:longitud>')
def generar_contrasena(longitud):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return f"Contraseña generada: {contrasena}"

if __name__ == "__main__":
    app.run(debug=True)