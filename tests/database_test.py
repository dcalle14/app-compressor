import unittest
import psycopg2
from psycopg2.errors import *
import sys
sys.path.append('.')
import secretconfige

# Agregamos la ruta raíz del proyecto


# Importamos los controladores y modelos correctamente
from src.controller.controlador_tabla import ControladorPalabrasComprimidas
from src.model.palabra_comprimida import PalabraComprimida

class ControladorPalabrasComprimidasTestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Elimina y crea la tabla antes de ejecutar las pruebas"""
        ControladorPalabrasComprimidas.EliminarTabla()
        ControladorPalabrasComprimidas.CrearTabla()

    @staticmethod
    def ObtenerCursor():
        """Crea la conexión a la base de datos y retorna un cursor para hacer consultas"""
        connection = psycopg2.connect(
            database=secretconfige.PGDATABASE, 
            user=secretconfige.PGUSER, 
            password=secretconfige.PGPASSWORD, 
            host=secretconfige.PGHOST, 
            port=secretconfige.PGPORT
        )
        return connection.cursor()

    def test_crear_tabla(self):
        """Valida que la tabla de palabras comprimidas se haya creado correctamente"""
        cursor = self.ObtenerCursor()
        cursor.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'palabras_comprimidas');")
        tabla_existe = cursor.fetchone()[0]
        self.assertTrue(tabla_existe)

    def test_insertar_palabra(self):
        """Valida que se pueda insertar una palabra comprimida en la base de datos"""
        palabra = PalabraComprimida("original", "comprimida")
        id = ControladorPalabrasComprimidas.InsertarPalabra(palabra)
        self.assertIsNotNone(id)

    def test_buscar_palabra_por_id(self):
        """Valida que se pueda buscar una palabra comprimida por su ID"""
        palabra = PalabraComprimida("original2", "comprimida2")
        id_insertado = ControladorPalabrasComprimidas.InsertarPalabra(palabra)
        palabra_encontrada = ControladorPalabrasComprimidas.BuscarPalabraPorID(id_insertado)
        self.assertIsNotNone(palabra_encontrada)
        self.assertEqual(palabra_encontrada.palabra_original, "original2")

    def test_actualizar_palabra(self):
        """Valida que se pueda actualizar una palabra comprimida"""
        palabra = PalabraComprimida("original3", "comprimida3")
        id_insertado = ControladorPalabrasComprimidas.InsertarPalabra(palabra)
        actualizado = ControladorPalabrasComprimidas.ActualizarPalabra(id_insertado, "actualizada", "original_actualizada")
        self.assertTrue(actualizado)

    def test_eliminar_palabra_por_id(self):
        """Valida que se pueda eliminar una palabra comprimida por ID"""
        palabra = PalabraComprimida("original4", "comprimida4")
        id_insertado = ControladorPalabrasComprimidas.InsertarPalabra(palabra)
        eliminado = ControladorPalabrasComprimidas.EliminarPalabraPorID(id_insertado)
        self.assertTrue(eliminado)

if __name__ == '__main__':
    unittest.main()
