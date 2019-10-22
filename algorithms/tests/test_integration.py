import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import sorting_functions
import unittest

class algorithms_test_case(unittest.TestCase):

    def test_merge_sort(self):

        # data
        input_list1 = [1, 2] # [1, 2]
        input_list2 = [2, 1] # [1, 2]
        input_list3 = [] # []
        input_list4 = [1] # [1]
        input_list5 = [5, 1, 1] # [1, 1, 5]
        input_list6 = [9, 1, 10, 2] # [1, 2, 9, 10]
        input_list7 = range(10)[::-1] #list(range(10))

        # results
        result1 = sorting_functions.merge_sort( input_list1 )
        result2 = sorting_functions.merge_sort( input_list2 )
        result3 = sorting_functions.merge_sort( input_list3 )
        result4 = sorting_functions.merge_sort( input_list4 )
        result5 = sorting_functions.merge_sort( input_list5 )
        result6 = sorting_functions.merge_sort( input_list6 )
        result7 = sorting_functions.merge_sort( input_list7 )
        
        # test
        self.assertEqual ( result1 , [1, 2] )
        self.assertEqual ( result2 , [1, 2] )
        self.assertEqual ( result3 , [] )
        self.assertEqual ( result4 , [1] )
        self.assertEqual ( result5 , [1, 1, 5] )
        self.assertEqual ( result6 , [1, 2, 9, 10] )
        self.assertEqual ( result7 , list(range(10)) )

if __name__ == '__main__':
    unittest.main()