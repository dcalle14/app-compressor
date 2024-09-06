import sys
sys.path.append("src")

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
    print("Welcome to the Text Compressor and Decompressor!")
    print("-------------------------------------------------")
    
    while True:
        print("\nPlease choose an option:")
        print("1. Compress text")
        print("2. Decompress text")
        print("3. Leave")
        
        opcion = input("Enter the number of the desired option: ")
        
        if opcion == "1":
            try:
                data = input("\nWrite the text you want to compress: ")
                if data.isdigit(): # Check if it is an integer
                    raise RLECompressionIntegerError("Cannot compress an integer.")
                elif data == "":  # Check if the string is empty
                    raise RLECompressionNoneError("Input cannot be empty or None.")
                
                compressed_data = rle_encode(data)
                print(f"Compressed text: {compressed_data}")
                
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
            print("\nThank you for using the Text Compressor and Decompressor! See you later!")
            break
        
        else:
            print("\nInvalid option. Please type the number you want in the given options.")

if __name__ == "__main__":
    main()
