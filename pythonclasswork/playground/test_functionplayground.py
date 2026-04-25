import unittest
import fuctionplayground

class TestCubeFunction(unittest.TestCase):
    def test_that_cube_function_exists(self):
        fuctionplayground.cube(3)
        
    def test_that_cube_function_return_correct_result(self):
        actual = fuctionplayground.cube(3)
        expected = 27
        self.assertEqual(actual, expected)
        actual = fuctionplayground.cube(5)
        expected = 125
        self.assertEqual(actual, expected)
        
    def test_that_cube_function_return_invalid_data_type_with_wrong_input(self):
        actual = fuctionplayground.cube("musa")
        expected = "invalid input"
        self.assertEqual(actual, expected)
