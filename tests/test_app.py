import sys
import os
# Add the src directory to the Python path for module imports
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

import unittest
from functionalities.app import app 
from model.rle_compression import RLECompression
from controller.table_controller import TableController

"""
we use self.assertEqual: Compares expected values ​​with actual results to ensure that functions return correct results
self.assertIn: Verifies that a specific value is contained within a result.
self.assertIsInstance: Confirms that an object is of a specific data type.
self.assertTrue: Ensures that a condition is true.

"""

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        # Configure Flask test client
        self.app = app.test_client()
        self.app.testing = True

    def test_index_page_load(self):
        # Verify that the main page loads correctly
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        # Ensure page contains expected title text
        self.assertIn('Aplicación de Compresión y Tablas', response.get_data(as_text=True))


class RLECompressionTestCase(unittest.TestCase):
    def setUp(self):
        # Initialize RLECompression instance for tests
        self.rle = RLECompression()

    def test_compress_empty_string(self):
        # Test RLE compression with an empty string
        result = self.rle.compress('')
        self.assertEqual(result, '', "Compressing an empty string should return an empty string.")

    def test_compress_repeating_pattern(self):
        # Test RLE compression with a standard repeating pattern
        result = self.rle.compress('AAABBBCC')
        self.assertEqual(result, '3A3B2C', "RLE compression of 'AAABBBCC' should be '3A3B2C'.")

    def test_compress_single_character(self):
        # Test RLE compression with a single character input
        result = self.rle.compress('A')
        self.assertEqual(result, '1A', "RLE compression of 'A' should be '1A'.")

    def test_compress_unique_characters(self):
        # Test RLE compression with unique characters
        result = self.rle.compress('ABC')
        self.assertEqual(result, '1A1B1C', "RLE compression of 'ABC' should be '1A1B1C'.")

class TableControllerTestCase(unittest.TestCase):
    def setUp(self):
        # Initialize TableController instance for tests
        self.table_controller = TableController()

    def test_get_data_format(self):
        # Verify that the table controller returns data in list format
        table_data = self.table_controller.get_data()
        self.assertIsInstance(table_data, list, "The result should be a list.")
        self.assertTrue(len(table_data) > 0, "The list of data should not be empty.")
        self.assertIsInstance(table_data[0], tuple, "Each entry in the data should be a tuple.")

    def test_data_content_structure(self):
        # Ensure the data format in each row is as expected
        table_data = self.table_controller.get_data()
        for row in table_data:
            # Validate each row has exactly two elements
            self.assertEqual(len(row), 2, "Each row in the table should have exactly 2 elements.")
            # Check if the first element is a string
            self.assertIsInstance(row[0], str, "The first element of each row should be a string.")
            # Check if the second element is a numeric type (int or float)
            self.assertIsInstance(row[1], (int, float), "The second element of each row should be a number.")
    
    def test_filter_data_by_value(self):
        # Verificar si el controlador de tablas puede filtrar datos correctamente
        filtered_data = self.table_controller.filter_data_by_value(min_value=50)
        self.assertIsInstance(filtered_data, list, "El resultado debería ser una lista.")
        for row in filtered_data:
            # Asegurarse de que cada valor filtrado cumple con el criterio de ser mayor o igual al valor mínimo
            self.assertGreaterEqual(row[1], 50, "El valor de la segunda columna debe ser mayor o igual a 50.")

if __name__ == '__main__':
    # Run all tests
    unittest.main()
