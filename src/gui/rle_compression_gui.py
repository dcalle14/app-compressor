import sys
import os

# Add the project root path to sys.path
# Agrega la ruta raíz del proyecto al sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from src.functionalities.rle_compression import (
    rle_encode, 
    rle_decode, 
    RLECompressionNoneError, 
    RLECompressionIntegerError, 
    RLECompressionListError, 
    RLECompressionDictError, 
    RLECompressionNegativeValueError, 
    RLECompressionZeroCountError
)

class RLECompressionApp(App):
    def build(self):
        # Set the background color to a dark gray (close to black)
        # Establecer el color de fondo a gris oscuro (cercano a negro)
        Window.clearcolor = (0.1, 0.1, 0.1, 1)  # Fondo gris oscuro

        # Create the main layout with padding and spacing
        # Crear el layout principal con padding y espacio
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Label for text input (title for the input section)
        # Etiqueta para el campo de texto (título para la sección de entrada)
        self.label_input = Label(text='Enter the text of the desired option:', color=(1, 1, 1, 1))  # Texto blanco
        self.layout.add_widget(self.label_input)

        # Text input field
        # Campo de entrada de texto
        self.text_input = TextInput(
            multiline=False, 
            background_color=(0.9, 0.9, 0.9, 1),  # Fondo gris claro
            foreground_color=(0, 0, 0, 1)         # Texto negro
        )
        self.layout.add_widget(self.text_input)

        # Compress button with light gray background and black text
        # Botón de compresión con fondo gris claro y texto negro
        self.compress_button = Button(
            text='Compress', 
            background_color=(0.7, 0.7, 0.7, 1),  # Gris claro
            color=(0, 0, 0, 1)                    # Texto negro
        )
        self.compress_button.bind(on_press=self.compress_text)
        self.layout.add_widget(self.compress_button)

        # Label to display the compressed result
        # Etiqueta para mostrar el resultado comprimido
        self.compressed_label = Label(text='Compressed result:', color=(1, 1, 1, 1))  # Texto blanco
        self.layout.add_widget(self.compressed_label)

        # Label for the compressed output (display area)
        # Etiqueta para mostrar el resultado comprimido
        self.compressed_output = Label(
            text='', 
            size_hint_y=None, 
            height=40, 
            color=(1, 1, 1, 1)                    # Texto blanco
        )
        self.layout.add_widget(self.compressed_output)

        # Decompress button with light gray background and black text
        # Botón de descompresión con fondo gris claro y texto negro
        self.decompress_button = Button(
            text='Decompress', 
            background_color=(0.7, 0.7, 0.7, 1),  # Gris claro
            color=(0, 0, 0, 1)                    # Texto negro
        )
        self.decompress_button.bind(on_press=self.decompress_text)
        self.layout.add_widget(self.decompress_button)

        # Label to display the decompressed result
        # Etiqueta para mostrar el resultado descomprimido
        self.decompressed_label = Label(text='Decompressed result:', color=(1, 1, 1, 1))  # Texto blanco
        self.layout.add_widget(self.decompressed_label)

        # Label for the decompressed output (display area)
        # Etiqueta para mostrar el resultado descomprimido
        self.decompressed_output = Label(
            text='', 
            size_hint_y=None, 
            height=40, 
            color=(1, 1, 1, 1)                    # Texto blanco
        )
        self.layout.add_widget(self.decompressed_output)

        # Error message label
        # Etiqueta para mostrar mensajes de error
        self.error_label = Label(text='', color=(1, 0, 0, 1), size_hint_y=None, height=40)  # Texto rojo para errores
        self.layout.add_widget(self.error_label)

        return self.layout

    def compress_text(self, instance):
        try:
            input_text = self.text_input.text
            compressed_text = rle_encode(input_text)  # Usa la función de compresión
            self.compressed_output.text = compressed_text
            self.error_label.text = ''  # Limpiar el mensaje de error si no hay errores
        except (RLECompressionNoneError, RLECompressionIntegerError, RLECompressionListError, RLECompressionDictError) as e:
            self.error_label.text = f"Compression Error: {str(e)}"  # Mostrar el mensaje de error

    def decompress_text(self, instance):
        try:
            compressed_text = self.compressed_output.text
            decompressed_text = rle_decode(compressed_text)  # Usa la función de descompresión
            self.decompressed_output.text = decompressed_text
            self.error_label.text = ''  # Limpiar el mensaje de error si no hay errores
        except (RLECompressionNoneError, RLECompressionIntegerError, RLECompressionNegativeValueError, RLECompressionZeroCountError) as e:
            self.error_label.text = f"Decompression Error: {str(e)}"  # Mostrar el mensaje de error


if __name__ == '__main__':
    # Set the window title and logo before the app starts
    # Establecer el título y el logo de la ventana antes de iniciar la app
    Window.title = "TEXT COMPRESSOR"
    Window.icon = "C:/Workspace/Clean Code/text-compressor/LogoTextCompressor.png"

    RLECompressionApp().run()
