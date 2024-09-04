class RLECompressionError(Exception): # Clase base para excepciones en el módulo de compresión RLE.
    pass

class RLECompressionTypeError(RLECompressionError): # Se lanza cuando se proporciona un tipo de entrada no válido.
    pass

class RLECompressionValueError(RLECompressionError): # Se lanza cuando se encuentra un valor incorrecto en la entrada.
    pass

def rle_encode(data: str) -> str:
    """
    This part of the code is for
    """

    if not isinstance(data, str):
        raise RLECompressionTypeError("La entrada debe ser una cadena de texto")
    
    if data.isdigit():
        raise RLECompressionTypeError("La entrada no debe ser solo numérica")

    if data is None or data == "":
        raise RLECompressionTypeError("No hay texto, ingresa nuevamente")

    encoded = ""
    i = 0
    length = len(data)
    
    while i < length:
        count = 1
        while i + 1 < length and data[i] == data[i + 1]:
            i += 1
            count += 1
        encoded += data[i] + (str(count) if count > 1 else "")
        i += 1
    
    return encoded

def rle_decode(data: str) -> str:
    """
    This part of the code is for
    """
    
    if not isinstance(data, str):
        raise RLECompressionTypeError("La entrada debe ser una cadena de texto")
    
    if data.isdigit():
        raise RLECompressionTypeError("La entrada no debe ser solo numérica")
    
    if data is None or data == "":
        raise RLECompressionTypeError("No hay texto, ingresa nuevamente")

    decoded = ""
    i = 0
    length = len(data)
    
    while i < length:
        char = data[i]
        i += 1
        count_str = ""
        while i < length and data[i].isdigit():
            count_str += data[i]
            i += 1
        
        if count_str and int(count_str) <= 0:
            raise RLECompressionValueError("El recuento de repeticiones debe ser mayor a cero")
        
        if i < length and data[i] == '-':
            raise RLECompressionValueError("El texto comprimido es incorrecto, no se permiten números negativos")
        
        count = int(count_str) if count_str else 1
        decoded += char * count
    
    return decoded
