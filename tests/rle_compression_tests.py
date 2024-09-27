import unittest
import sys

# Asegúrate de que la ruta sea correcta para encontrar el módulo en la estructura de carpetas.
sys.path.append('src/functionalities')

from rle_compression import (
    rle_encode,
    rle_decode,
    RLECompressionNoneError,
    RLECompressionIntegerError,
    RLECompressionListError,
    RLECompressionDictError,
    RLECompressionNegativeValueError,
    RLECompressionZeroCountError
)

class TestRLECompression(unittest.TestCase):

    """
    We use the AssertEqual function to call the functionality where an input data by the user is 
    compressed and decompressed and using a comma we place the expected result, returning a boolean value.
    """

    # Normal cases for compression.
    def test_rle_encode_normal1(self):
        self.assertEqual(rle_encode("AAAABBBCCC"), "A4B3C3")

    def test_rle_encode_normal2(self):
        self.assertEqual(rle_encode("abcd"), "abcd")

    def test_rle_encode_normal3(self):
        self.assertEqual(rle_encode("aaBBcc"), "a2B2c2")

   # Normal cases for decompress.
    def test_rle_decode_normal1(self):
        self.assertEqual(rle_decode("A4B3C3"), "AAAABBBCCC")

    def test_rle_decode_normal2(self):
        self.assertEqual(rle_decode("abcd"), "abcd")

    def test_rle_decode_normal3(self):    
        self.assertEqual(rle_decode("a2B2c2"), "aaBBcc")

    # Extraordinary cases to compress.
    def test_rle_encode_extraordinary1(self):
        self.assertEqual(rle_encode("sasa"), "sasa")

    def test_rle_encode_extraordinary2(self):    
        self.assertEqual(rle_encode("a"), "a")

    def test_rle_encode_extraordinary3(self):
        self.assertEqual(rle_encode("aaaaaaaaaaaaaaaaaaaaaaaa"), "a24")

    # Extraordinary cases to decompress.
    def test_rle_decode_extraordinary1(self):
        self.assertEqual(rle_decode("sasa"), "sasa")
    
    def test_rle_decode_extraordinary2(self):
        self.assertEqual(rle_decode("a"), "a")

    def test_rle_decode_extraordinary3(self):    
        self.assertEqual(rle_decode("a24"), "aaaaaaaaaaaaaaaaaaaaaaaa")

    # Error cases for compressing.
    def test_rle_encode_error_1(self):
        with self.assertRaises(RLECompressionNoneError):
            rle_encode(None)  # Try to compress a None

    def test_rle_encode_error_2(self):
        with self.assertRaises(RLECompressionIntegerError):
            rle_encode(12345)  # Try to compress an integer

    def test_rle_encode_error_3(self):
        with self.assertRaises(RLECompressionListError):
            rle_encode(["a", "b", "c"])  # Try to compress a list

    def test_rle_encode_error_4(self):
        with self.assertRaises(RLECompressionDictError):
            rle_encode({"a": 1})  # Try to compress a dictionary

    # Error cases for decompressing.
    def test_rle_decode_error_1(self):
        with self.assertRaises(RLECompressionNegativeValueError):
            rle_decode("a3b-2")  # Try to decompress a malformed string (negative number)

    def test_rle_decode_error_2(self):
        with self.assertRaises(RLECompressionZeroCountError):
            rle_decode("a10b0")  # Try to decompress with zero count format (should not be allowed)

    def test_rle_decode_error_3(self):
        with self.assertRaises(RLECompressionNoneError):
            rle_decode(None)  # Try to decompress a None 

    def test_rle_decode_error_4(self):
        with self.assertRaises(RLECompressionIntegerError):
            rle_decode(12345)  # Try to decompress an integer

# This code snippet allows the test to be run individually.
if __name__ == "__main__":
    unittest.main()
