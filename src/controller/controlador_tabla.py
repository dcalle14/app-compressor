import sys
sys.path.append("src")

import psycopg2
from model.palabra_comprimida import PalabraComprimida
import SecretConfig

class ControladorPalabrasComprimidas:

    @staticmethod
    def CrearTabla():
        """ Crea la tabla de palabras comprimidas en la BD """
        cursor = ControladorPalabrasComprimidas.ObtenerCursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS palabras_comprimidas (
                id SERIAL PRIMARY KEY,
                palabra_original TEXT NOT NULL,
                palabra_comprimida TEXT NOT NULL
            );
        """)
        cursor.connection.commit()

    @staticmethod
    def EliminarTabla():
        """ Borra la tabla de palabras comprimidas de la BD """
        cursor = ControladorPalabrasComprimidas.ObtenerCursor()

        cursor.execute("DROP TABLE IF EXISTS palabras_comprimidas")
        cursor.connection.commit()

    @staticmethod
    def InsertarPalabra(palabra_comprimida: PalabraComprimida):
        """ Recibe una instancia de la clase PalabraComprimida y la inserta en la tabla respectiva """
        cursor = ControladorPalabrasComprimidas.ObtenerCursor()

        cursor.execute(f"""
            INSERT INTO palabras_comprimidas (palabra_original, palabra_comprimida) 
            VALUES ('{palabra_comprimida.palabra_original}', '{palabra_comprimida.palabra_comprimida}')
            RETURNING id;
        """)
        cursor.connection.commit()
        id = cursor.fetchone()[0]
        return id

    @staticmethod
    def BuscarPalabraPorID(identificacion):
        """ Trae una palabra comprimida de la tabla palabras_comprimidas por el ID """
        cursor = ControladorPalabrasComprimidas.ObtenerCursor()

        cursor.execute(f"""
            SELECT id, palabra_original, palabra_comprimida 
            FROM palabras_comprimidas 
            WHERE id = {identificacion}
        """)
        fila = cursor.fetchone()
        if fila:
            resultado = PalabraComprimida(id=fila[0], palabra_original=fila[1], palabra_comprimida=fila[2])
            return resultado
        return False

    @staticmethod
    def ActualizarPalabra(id, nueva_palabra_comprimida, nueva_palabra_original):
        """ Actualiza la palabra comprimida de un registro específico por ID """
        cursor = ControladorPalabrasComprimidas.ObtenerCursor()

        cursor.execute(f"""
            UPDATE palabras_comprimidas
            SET palabra_comprimida = '{nueva_palabra_comprimida}',
            palabra_original = '{nueva_palabra_original}'
            WHERE id = {id};
        """)
        cursor.connection.commit()
        affected_rows : int = cursor.rowcount
        if affected_rows >=1 :
            return True
        else:
            return False
    @staticmethod
    def EliminarPalabraPorID(id):
        """ Elimina un registro específico de la tabla por ID """
        cursor = ControladorPalabrasComprimidas.ObtenerCursor()

        cursor.execute(f"""
            DELETE FROM palabras_comprimidas
            WHERE id = {id};
        """)
        affected_rows : int = cursor.rowcount
        cursor.connection.commit()
        if affected_rows >=1 :
            return True
        else:
            return False


    @staticmethod
    def ObtenerCursor():
        """ Crea la conexión a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(
            database=SecretConfig.PGDATABASE, 
            user=SecretConfig.PGUSER, 
            password=SecretConfig.PGPASSWORD, 
            host=SecretConfig.PGHOST, 
            port=SecretConfig.PGPORT
        )
        cursor = connection.cursor()
        return cursor
