from rle_compression import rle_encode, rle_decode, RLECompressionTypeError, RLECompressionValueError

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
                compressed_data = rle_encode(data)
                print(f"Compressed text: {compressed_data}")
            except (RLECompressionTypeError, RLECompressionValueError) as e:
                print(f"Error: {e}")
        
        elif opcion == "2":
            try:
                compressed_data = input("\nType the compressed text you want to decompress: ")
                decompressed_data = rle_decode(compressed_data)
                print(f"Decompressed text: {decompressed_data}")
            except (RLECompressionTypeError, RLECompressionValueError) as e:
                print(f"Error: {e}")
        
        elif opcion == "3":
            print("\nThank you for using the Text Compressor and Decompressor! See you later!")
            break
        
        else:
            print("\nInvalid option. Please type the number you want in the given options.")

if __name__ == "__main__":
    main()
