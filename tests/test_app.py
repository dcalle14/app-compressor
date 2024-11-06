import unittest
from app import app
from model.rle_compression import RLECompression
from controller.table_controller import TableController

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        # Configures the Flask test client
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        # Test to verify that the main page loads correctly
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Compression and Tables Application', response.get_data(as_text=True))

    def test_compress(self):
        # Test to verify the compression functionality
        response = self.app.post('/compress', data={'text': 'AAABBBCC'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Compression Result:', response.get_data(as_text=True))
        self.assertIn('3A3B2C', response.get_data(as_text=True))  # Checks if the result is correct

class RLECompressionTestCase(unittest.TestCase):
    def setUp(self):
        # Instance of RLECompression for testing
        self.rle = RLECompression()

    def test_rle_compression_empty(self):
        # Test RLE compression with an empty string
        result = self.rle.compress('')
        self.assertEqual(result, '', "Compressing an empty string should return an empty string.")

    def test_rle_compression_basic(self):
        # Test RLE compression with a basic string
        result = self.rle.compress('AAABBBCC')
        self.assertEqual(result, '3A3B2C', "RLE compression of 'AAABBBCC' should be '3A3B2C'.")

    def test_rle_compression_single_character(self):
        # Test RLE compression with a single character
        result = self.rle.compress('A')
        self.assertEqual(result, '1A', "RLE compression of 'A' should be '1A'.")

    def test_rle_compression_no_repeats(self):
        # Test RLE compression with non-repeating characters
        result = self.rle.compress('ABC')
        self.assertEqual(result, '1A1B1C', "RLE compression of 'ABC' should be '1A1B1C'.")

class TableControllerTestCase(unittest.TestCase):
    def setUp(self):
        # Instance of TableController for testing
        self.table_controller = TableController()

    def test_table_get_data(self):
        # Test that the table controller returns data correctly
        table_data = self.table_controller.get_data()
        self.assertIsInstance(table_data, list, "The result should be a list.")
        self.assertTrue(len(table_data) > 0, "The list of data should not be empty.")
        self.assertIsInstance(table_data[0], tuple, "Each entry in the data should be a tuple.")

    def test_table_data_content(self):
        # Test that the table data contains the expected format
        table_data = self.table_controller.get_data()
        for row in table_data:
            self.assertEqual(len(row), 2, "Each row in the table should have exactly 2 elements.")
            self.assertIsInstance(row[0], str, "The first element of each row should be a string.")
            self.assertIsInstance(row[1], (int, float), "The second element of each row should be a number.")

if __name__ == '__main__':
    unittest.main()

