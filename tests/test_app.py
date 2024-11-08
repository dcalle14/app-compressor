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
        self.app = app.test_client()
        self.app.testing = True


    def test_empty_compress_request(self):
        # Test compression with empty input
        response = self.app.post('/compress', data={'text': ''})
        self.assertEqual(response.status_code, 302)  # Redirect expected

    def test_decompress_endpoint(self):
        # Test successful decompression
        response = self.app.post('/decompress', data={'compressed_text': '3A3B'})
        self.assertEqual(response.status_code, 302)  # Redirect expected

class RLECompressionTestCase(unittest.TestCase):
    def setUp(self):
        self.rle = RLECompression()

    def test_compress_empty_string(self):
        result = self.rle.compress('')
        self.assertEqual(result, '')

    def test_compress_repeating_pattern(self):
        result = self.rle.compress('AAABBBCC')
        self.assertEqual(result, '3A3B2C')

    def test_compress_single_character(self):
        result = self.rle.compress('A')
        self.assertEqual(result, '1A')

    def test_compress_unique_characters(self):
        result = self.rle.compress('ABC')
        self.assertEqual(result, '1A1B1C')

    def test_compress_with_numbers(self):
        # Test compression with numbers in input
        result = self.rle.compress('111222')
        self.assertEqual(result, '3132')

    def test_compress_mixed_case(self):
        # Test compression with mixed case letters
        result = self.rle.compress('aaaBBBccc')
        self.assertEqual(result, '3a3B3c')

    def test_compress_special_characters(self):
        # Test compression with special characters
        result = self.rle.compress('###@@@!!!')
        self.assertEqual(result, '3#3@3!')

class TableControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.table_controller = TableController()

    def test_get_data_format(self):
        table_data = self.table_controller.get_data()
        self.assertIsInstance(table_data, list)
        self.assertTrue(len(table_data) > 0)
        self.assertIsInstance(table_data[0], tuple)

    def test_data_content_structure(self):
        table_data = self.table_controller.get_data()
        for row in table_data:
            self.assertEqual(len(row), 2)
            self.assertIsInstance(row[0], str)
            self.assertIsInstance(row[1], (int, float))

    def test_filter_data_by_value(self):
        filtered_data = self.table_controller.filter_data_by_value(min_value=50)
        self.assertIsInstance(filtered_data, list)
        for row in filtered_data:
            self.assertGreaterEqual(row[1], 50)

    def test_empty_filter_result(self):
        # Test filtering with a value that should return no results
        filtered_data = self.table_controller.filter_data_by_value(min_value=99999)
        self.assertEqual(len(filtered_data), 0)

    def test_negative_filter_value(self):
        # Test filtering with negative values
        filtered_data = self.table_controller.filter_data_by_value(min_value=-1)
        self.assertEqual(len(filtered_data), len(self.table_controller.get_data()))

class RLEErrorHandlingTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_invalid_compressed_format(self):
        # Test decompression with invalid format
        response = self.app.post('/decompress', data={'compressed_text': 'invalid3A'})
        self.assertEqual(response.status_code, 302)  # Redirect expected


if __name__ == '__main__':
    unittest.main()