class RLECompressionError(Exception):
    """Clase base para excepciones en el módulo de compresión RLE."""
    pass

class RLECompressionNoneError(RLECompressionError):
    """Se lanza cuando la entrada es None."""
    pass

class RLECompressionIntegerError(RLECompressionError):
    """Se lanza cuando la entrada es un número entero."""
    pass

class RLECompressionListError(RLECompressionError):
    """Se lanza cuando la entrada es una lista."""
    pass

class RLECompressionDictError(RLECompressionError):
    """Se lanza cuando la entrada es un diccionario."""
    pass

class RLECompressionNegativeValueError(RLECompressionError):
    """Se lanza cuando la entrada contiene un número negativo."""
    pass

class RLECompressionZeroCountError(RLECompressionError):
    """Se lanza cuando la entrada contiene un conteo de cero."""
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
        raise RLECompressionNoneError("No se puede comprimir un valor None.")
    if isinstance(data, int):
        raise RLECompressionIntegerError("No se puede comprimir un número entero.")
    if isinstance(data, list):
        raise RLECompressionListError("No se puede comprimir una lista.")
    if isinstance(data, dict):
        raise RLECompressionDictError("No se puede comprimir un diccionario.")
    
    # Lógica de compresión RLE
    compressed = []
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count += 1
            i += 1
        compressed.append(f"{data[i]}{count}" if count > 1 else data[i])
        i += 1
    return ''.join(compressed)


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
            raise RLECompressionNoneError("No se puede descomprimir un valor None.")
    
    if isinstance(data, int):
            raise RLECompressionIntegerError("No se puede descomprimir un número entero.")
    
    if "-" in data:
         raise RLECompressionNegativeValueError("Cannot decode negative numbers.")
        
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
                    raise RLECompressionNegativeValueError("El valor de repetición no puede ser negativo.")
                if count == 0:
                    raise RLECompressionZeroCountError("El valor de repetición no puede ser cero.")
            decompressed.append(char * count)
            i += 1
    return ''.join(decompressed)
    