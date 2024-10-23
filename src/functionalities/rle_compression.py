from controller.controlador_tabla import ControladorPalabrasComprimidas as cursor
from model.palabra_comprimida import PalabraComprimida

class RLECompressionError(Exception):
    """Base class for exceptions in the RLE compression module"""
    pass

class RLECompressionNoneError(RLECompressionError):
    """Thrown when input is None"""
    pass

class RLECompressionIntegerError(RLECompressionError):
    """Thrown when the input is an integer"""
    pass

class RLECompressionListError(RLECompressionError):
    """Thrown when the input is a list"""
    pass

class RLECompressionDictError(RLECompressionError):
    """Thrown when the input is a dictionary"""
    pass

class RLECompressionNegativeValueError(RLECompressionError):
    """Thrown when the input contains a negative number"""
    pass

class RLECompressionZeroCountError(RLECompressionError):
    """Thrown when the input contains a zero count"""
    pass

def rle_encode(data: str) -> str:
    """
    Compresses a text string using the Run-Length Encoding (RLE) technique.

    This function takes a text string and compresses sequences of repeated characters
    into a single character followed by the number of repetitions. For example, the string
    "aaabbc" would be compressed to "a3b2c".

    Parameters:
    data (str): The text string to compress.

    Returns:
    str: The string compressed using RLE.
    """
    if data is None:
        raise RLECompressionNoneError("You cannot compress a None value.")
    
    if isinstance(data, int):
        raise RLECompressionIntegerError("You cannot compress an integer.")
    
    if isinstance(data, list):
        raise RLECompressionListError("You cannot compress a list.")
    
    if isinstance(data, dict):
        raise RLECompressionDictError("You cannot compress a dictionary.")
    compressed = []
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count += 1
            i += 1
        compressed.append(f"{data[i]}{count}" if count > 1 else data[i])
        i += 1
    compressed_str : str = ''.join(compressed)

    return compressed_str


def rle_decode(data: str) -> str:
    """
    Decompresses a text string that has been compressed using the Run-Length Encoding (RLE) technique.

    This function takes a compressed text string and expands it back to its original form.
    For example, the string "a3b2c" would be decompressed to "aaabbc".

    Parameters:
    data (str): The compressed text string to be decompressed.

    Returns:
    str: The decompressed text string.
    """

    if data is None:
            raise RLECompressionNoneError("Cannot decompress a value of None.")
    
    if isinstance(data, int):
            raise RLECompressionIntegerError("Cannot decompress an integer.")
    
    if "-" in data:
         raise RLECompressionNegativeValueError("Cannot decompress negative numbers")
        
    decompressed = []
    i = 0
    while i < len(data):
            char = data[i]
            count = 1
            if i + 1 < len(data) and (data[i + 1].isdigit() or (data[i + 1] == '-' and data[i + 2].isdigit())):
                count_str = ''
                while i + 1 < len(data) and (data[i + 1].isdigit() or (data[i + 1] == '-' and data[i + 2].isdigit())):
                    count_str += data[i + 1]
                    i += 1
                count = int(count_str)
                if count < 0:
                    raise RLECompressionNegativeValueError("The repetition value cannot be negative.")
                if count == 0:
                    raise RLECompressionZeroCountError("The repeat value cannot be zero.")
            decompressed.append(char * count)
            i += 1
    return ''.join(decompressed)
    