import unittest # Importamos la libreria unittest que nos brinda las funcionalidades para realizar las pruebas.
from rle_compression import rle_encode, rle_decode, RLECompressionTypeError, RLECompressionValueError
class TestRLECompression(unittest.TestCase):

    # Casos Normales para comprimir.
    def test_rle_encode_normal1(self):
        self.assertEqual(rle_encode("AAAABBBCCC"), "A4B3C3")

    def test_rle_encode_normal2(self):
        self.assertEqual(rle_encode("abcd"), "abcd")

    def test_rle_encode_normal3(self):
        self.assertEqual(rle_encode("aaBBcc"), "a2B2c2")

    # Casos Normales para descomprimir.
    def test_rle_decode_normal1(self):
        self.assertEqual(rle_decode("A4B3C3"), "AAAABBBCCC")

    def test_rle_decode_normal2(self):
        self.assertEqual(rle_decode("abcd"), "abcd")

    def test_rle_decode_normal3(self):    
        self.assertEqual(rle_decode("a2B2c2"), "aaBBcc")

    # Casos Extraordinarios para comprimir.
    def test_rle_encode_extraordinary1(self):
        self.assertEqual(rle_encode("sasa"), "sasa")

    def test_rle_encode_extraordinary2(self):    
        self.assertEqual(rle_encode("a"), "a")

    def test_rle_encode_extraordinary3(self):
        self.assertEqual(rle_encode("aaaaaaaaaaaaaaaaaaaaaaaa"), "a24")

    # Casos Extraordinarios para descomprimir.
    def test_rle_decode_extraordinary1(self):
        self.assertEqual(rle_decode("sasa"), "sasa")
    
    def test_rle_decode_extraordinary2(self):
        self.assertEqual(rle_decode("a"), "a")

    def test_rle_decode_extraordinary3(self):    
        self.assertEqual(rle_decode("a24"), "aaaaaaaaaaaaaaaaaaaaaaaa")

    # Casos de Error para comprimir.
    def test_rle_encode_error_1(self):
        with self.assertRaises(RLECompressionTypeError):
            rle_encode(None) # Intenta comprimir un None

    def test_rle_encode_error_2(self):
        with self.assertRaises(RLECompressionTypeError):
            rle_encode(12345) # Intenta comprimir un entero

    def test_rle_encode_error_3(self):
        with self.assertRaises(RLECompressionTypeError):
            rle_encode(["a", "b", "c"])  # Intenta comprimir una lista

    def test_rle_encode_error_4(self):
        with self.assertRaises(RLECompressionTypeError):
            rle_encode({"a": 1})  # Intenta comprimir un diccionario

    # Casos de Error para descomprimir.
    def test_rle_decode_error_1(self):
        with self.assertRaises(RLECompressionValueError):
            rle_decode("a3b-2")  # Intenta descomprimir una cadena de formato incorrecto (número negativo)

    def test_rle_decode_error_2(self):
        with self.assertRaises(RLECompressionValueError):
            rle_decode("a10b0")  # Intenta descomprimir con formato con recuento cero (no debería ser permitido)

    def test_rle_decode_error_3(self):
        with self.assertRaises(RLECompressionTypeError):
            rle_decode(None) # Intenta descomprimir un None

    def test_rle_decode_error_4(self):
        with self.assertRaises(RLECompressionTypeError):
            rle_decode(12345) # Intenta descomprimir un entero

# Este fragmento de código permite ejecutar la prueba individualmente.
if __name__ == "__main__":
    unittest.main()
