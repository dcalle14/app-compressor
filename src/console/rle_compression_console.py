import psycopg2
import sys


sys.path.append("src/")

from controller.controlador_tabla import ControladorPalabrasComprimidas as cursor
from model.palabra_comprimida import PalabraComprimida
from functionalities.rle_compression import (
    rle_encode,
    rle_decode,
    RLECompressionNoneError,
    RLECompressionIntegerError,
    RLECompressionListError,
    RLECompressionDictError,
    RLECompressionNegativeValueError,
    RLECompressionZeroCountError
)



def main():
    cursor.CrearTabla()


    print("Welcome to the Text Compressor and Decompressor!")
    print("-------------------------------------------------")
    
    while True:
        print("\nPlease choose an option:")
        print("1. Compress text")
        print("2. Decompress text")
        print("3. Delete word from database by id")
        print("4. Update word from database by id")
        print("5. Search word from database by id")
        print("6. Leave")
        
        opcion = input("Enter the number of the desired option: ")
        
        if opcion == "1":
            try:
                data = input("\nWrite the text you want to compress: ")
                if data.isdigit(): # Check if it is an integer
                    raise RLECompressionIntegerError("Cannot compress an integer.")
                elif data == "":  # Check if the string is empty
                    raise RLECompressionNoneError("Input cannot be empty or None.")
                
                compressed_data = rle_encode(data)
                palabra_comprimida = PalabraComprimida(data,compressed_data)
                id =  cursor.InsertarPalabra(palabra_comprimida)
                print(f"Compressed text: {compressed_data} with ID {id}")
                
            except RLECompressionNoneError:
                print("Error: The input cannot be None or an empty string.")
            except RLECompressionIntegerError:
                print("Error: The input cannot be an integer.")
            except RLECompressionListError:
                print("Error: The input cannot be a list.")
            except RLECompressionDictError:
                print("Error: The input cannot be a dictionary.")
        
        elif opcion == "2":
            try:
                compressed_data = input("\nType the compressed text you want to decompress: ")
                if compressed_data.isdigit(): # Check if it is an integer
                    raise RLECompressionIntegerError("Cannot decompress an integer.")
                elif compressed_data == "":  # Check if the string is empty
                    raise RLECompressionNoneError("Input cannot be empty or None.")
                
                decompressed_data = rle_decode(compressed_data)
                print(f"Decompressed text: {decompressed_data}")
                
            except RLECompressionNoneError:
                print("Error: The input cannot be None or an empty string.")
            except RLECompressionIntegerError:
                print("Error: The input cannot be an integer.")
            except RLECompressionNegativeValueError:
                print("Error: The input cannot contain negative repetition values.")
            except RLECompressionZeroCountError:
                print("Error: The input cannot contain zero as a repetition count.")
        

        elif opcion == "3":
            try:
                id = int(input("\nType the ID of the word you want to delete: "))
                if id == "":  # Check if the string is empty
                    raise RLECompressionNoneError("Input cannot be empty or None.")

                response = cursor.EliminarPalabraPorID(id)
                if response:
                    print(f"Word with ID {id} has been deleted successfully.")
                else:
                    print(f"Word with ID {id} was not found.")

            except RLECompressionNoneError:
                print("Error: The input cannot be None or an empty string.")
            except ValueError:
                print("Error: The input must be an integer.")

        elif opcion == "4":
            try:
                id = int(input("\nType the ID of the word you want to modify: "))
                new_original_word = input("\nType the new original word: ")

                if new_original_word.isdigit(): # Check if it is an integer
                    raise RLECompressionIntegerError("Cannot compress an integer.")
                if new_original_word == "":  # Check if the string is empty
                    raise RLECompressionNoneError("Input cannot be empty or None.")
                if id == "":  # Check if the string is empty
                    raise RLECompressionNoneError("Input cannot be empty or None.")

                compressed_str = rle_encode(new_original_word)
                response = cursor.ActualizarPalabra(id, compressed_str, new_original_word)
                if response:
                    print(f"Word with ID {id} has been updated successfully.")
                else:
                    print(f"Word with ID {id} was not found.")

            except RLECompressionNoneError:
                print("Error: The input cannot be None or an empty string.")
            except RLECompressionIntegerError:
                print("Error: The input cannot be an integer.")
            except ValueError:
                print("Error: The input must be an integer.")

        elif opcion == "5":
            try:
                id = int(input("\nType the ID of the word you want to search: "))
                if id == "":  # Check if the string is empty
                    raise RLECompressionNoneError("Input cannot be empty or None.")

                response = cursor.BuscarPalabraPorID(id)
                if response is False:
                    print(f"Word with ID {id} was not found.")
                else:
                    print(f"Word with ID {id} was found.")
                    print(f"Original word: {response.palabra_original}")
                    print(f"Compressed word: {response.palabra_comprimida}")

            except RLECompressionNoneError:
                print("Error: The input cannot be None or an empty string.")
            except ValueError:
                print("Error: The input must be an integer.")
        elif opcion == "6":
            print("\nThank you for using the Text Compressor and Decompressor! See you later!")
            break
        
        else:
            print("\nInvalid option. Please type the number you want in the given options.")

if __name__ == "__main__":
    main()
