import searching_functions
import sorting_functions
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

    def test_split_list_merge_sort(self):

        # data
        input_list_1 = [1, 2, 3]
        input_list_2 = [1, 2, 3, 4]
        input_list_3 = [1]
        input_list_4 = [1, 2, 3, 4, 5, 6, 7]

        # results
        result1 = sorting_functions.merge_sort_split_list( input_list_1 )
        result2 = sorting_functions.merge_sort_split_list( input_list_2 )
        result3 = sorting_functions.merge_sort_split_list( input_list_3 )
        result4 = sorting_functions.merge_sort_split_list( input_list_4 )

        # test
        self.assertEqual( result1 , ([1], [2, 3]) )
        self.assertEqual( result2 , ([1, 2], [3, 4]) )
        self.assertEqual( result3 , ([], [1]) )
        self.assertEqual( result4 , ([1, 2, 3], [4, 5, 6, 7]) )

    def test_merge_sort_merge_sorted_lists(self):
        
        # data
        left1, right1 = [1, 5], [3, 4]
        left2, right2 = [1, 2, 3], []

        # results
        result1 = sorting_functions.merge_sort_merge_sorted_list( left1, right1 )
        result2 = sorting_functions.merge_sort_merge_sorted_list( left2, right2 )

        # test
        self.assertEqual ( result1 , [1, 3, 4, 5] )
        self.assertEqual ( result2 , [1, 2, 3] )

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