import searching_functions
import unittest

# test the linear search function, searching for the element 1
class algorithms_test_case(unittest.TestCase):

    def test_linear_search(self):

        # unordered list of elements / DATA
        unordered_list = [99, 47, 63, 29, 16, 7, 92, 53, 39, 28, 1, 81, 69, 72]
        # run the function with data
        result = searching_functions.linear_search(1, unordered_list)
        # run the test
        self.assertEqual( result, 1 )

    def test_binary_search(self):

        # ordered list of elements
        ordered_list = [3, 5, 7, 9, 13, 22, 56, 78, 97, 104, 106, 222, 363, 651]
        # run the function with data
        result = searching_functions.binary_search(ordered_list, 104)
        # run the test
        self.assertEqual( result, 104 )

if __name__ == '__main__':
    unittest.main()