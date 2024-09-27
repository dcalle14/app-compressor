import sys
import os

# Agrega la ruta raíz del proyecto al sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from src.functionalities.rle_compression import rle_encode, rle_decode

class RLECompressionApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Etiqueta y campo de entrada de texto
        self.label_input = Label(text='Introduce el texto a comprimir:')
        self.text_input = TextInput(multiline=False)
        self.layout.add_widget(self.label_input)
        self.layout.add_widget(self.text_input)

        # Botón para comprimir
        self.compress_button = Button(text='Comprimir')
        self.compress_button.bind(on_press=self.compress_text)
        self.layout.add_widget(self.compress_button)

        # Etiqueta para mostrar el resultado comprimido
        self.compressed_label = Label(text='Resultado comprimido:')
        self.compressed_output = Label(text='', size_hint_y=None, height=40)
        self.layout.add_widget(self.compressed_label)
        self.layout.add_widget(self.compressed_output)

        # Botón para descomprimir
        self.decompress_button = Button(text='Descomprimir')
        self.decompress_button.bind(on_press=self.decompress_text)
        self.layout.add_widget(self.decompress_button)

        # Etiqueta para mostrar el resultado descomprimido
        self.decompressed_label = Label(text='Resultado descomprimido:')
        self.decompressed_output = Label(text='', size_hint_y=None, height=40)
        self.layout.add_widget(self.decompressed_label)
        self.layout.add_widget(self.decompressed_output)

        return self.layout

    def compress_text(self, instance):
        input_text = self.text_input.text
        compressed_text = rle_encode(input_text)  # Usa la función de compresión
        self.compressed_output.text = compressed_text

    def decompress_text(self, instance):
        compressed_text = self.compressed_output.text
        decompressed_text = rle_decode(compressed_text)  # Usa la función de descompresión
        self.decompressed_output.text = decompressed_text


if __name__ == '__main__':
    RLECompressionApp().run()
