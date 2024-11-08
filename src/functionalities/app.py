import sys
import os
import secrets
from werkzeug.utils import escape
from flask import Flask, render_template, request, redirect, url_for, flash

# Importa las clases y funciones necesarias
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
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
app.secret_key = secrets.token_hex(16)
text = escape(request.form.get('text', ''))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/compress', methods=['POST'])
def compress():
    text = request.form.get('text', '').strip()  # Usar strip() para eliminar espacios
    
    if not text:
        flash("Error: Por favor ingresa un texto para comprimir.", "error")
        return redirect(url_for('index'))
        
    try:
        compressed_data = rle_encode(text)
        palabra_comprimida = PalabraComprimida(text, compressed_data)
        id = cursor.InsertarPalabra(palabra_comprimida)
        flash(f"Texto comprimido exitosamente", "success")
        return render_template("index.html", 
                             compressed_result=compressed_data, 
                             original_text=text,
                             id=id)
    except Exception as e:
        flash(f"Error durante la compresión: {str(e)}", "error")
        return redirect(url_for('index'))
    
    
@app.route('/decompress', methods=['POST'])
def decompress():
    compressed_text = request.form.get('compressed_text')  # Obtener el texto comprimido
    if compressed_text:  # Verifica que el texto comprimido no esté vacío
        try:
            decompressed_data = rle_decode(compressed_text)
            flash(f"Texto descomprimido: {decompressed_data}", "success")
        except Exception as e:
            flash(f"Error: {str(e)}", "error")
    else:
        flash("Error: Por favor ingresa texto comprimido para descomprimir.", "error")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)

