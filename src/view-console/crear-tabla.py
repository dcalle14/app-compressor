import sys
sys.path.append("src")

from src.model.palabra_comprimida import PalabraComprimida  # Cambiamos Usuario por PalabraComprimida
from src.controller.controlador_tabla import ControladorPalabrasComprimidas  # Cambiamos ControladorUsuarios por ControladorPalabras

# Crear una instancia de PalabraComprimida
palabra = PalabraComprimida(identificacion=None, palabra_original="", palabra_comprimida="")

print("Por favor ingrese los datos de la palabra que desea crear")

# Recibir los datos de la palabra original y comprimida
palabra.palabra_original = input("Palabra original: ")
palabra.palabra_comprimida = input("Palabra comprimida: ")

# Insertar la palabra en la tabla
ControladorPalabrasComprimidas.InsertarPalabra(palabra)

print("Palabra insertada correctamente!")
