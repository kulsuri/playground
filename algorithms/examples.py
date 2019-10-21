import searching_functions

# unordered list of elements
unordered_list = [99, 47, 63, 29, 16, 7, 92, 53, 39, 28, 1, 81, 69, 72]

# ordered list of elements
ordered_list = [3, 5, 7, 9, 13, 22, 56, 78, 97, 104, 106, 222, 363, 651]

# call the linear search function, searching for the element 1
print( searching_functions.linear_search(1, unordered_list) )

# call the binary search function, searching for the element 104
print( searching_functions.binary_search(ordered_list, 104) )