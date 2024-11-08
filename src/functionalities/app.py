import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from flask import Flask, render_template, request, redirect, url_for, flash
from controller.controlador_tabla import ControladorPalabrasComprimidas as cursor
from model.palabra_comprimida import PalabraComprimida
from functionalities.rle_compression import (
    rle_encode,
    rle_decode,
    RLECompressionNoneError,
    RLECompressionIntegerError
)

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Cambia esto por una clave secreta

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/compress', methods=['POST'])
def compress():
    text = request.form['text']
    try:
        compressed_data = rle_encode(text)
        palabra_comprimida = PalabraComprimida(text, compressed_data)
        id = cursor.InsertarPalabra(palabra_comprimida)
        flash(f"Text compressed: {compressed_data} with ID {id}")
    except RLECompressionNoneError:
        flash("Error: The input cannot be None or an empty string.")
    except RLECompressionIntegerError:
        flash("Error: The input cannot be an integer.")
    return redirect(url_for('index'))

@app.route('/decompress', methods=['POST'])
def decompress():
    compressed_text = request.form['compressed_text']
    try:
        decompressed_data = rle_decode(compressed_text)
        flash(f"Decompressed text: {decompressed_data}")
    except Exception as e:
        flash(str(e))
    return redirect(url_for('index'))

# Añade más rutas para eliminar, actualizar y buscar según sea necesario

if __name__ == "__main__":
    app.run(debug=True)

