# Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

# For example, given the following matrix:

# [[1,  2,  3,  4,  5],
#  [6,  7,  8,  9,  10],
#  [11, 12, 13, 14, 15],
#  [16, 17, 18, 19, 20]]

# solution involves splitting the matrix using the pop() method with list comprehension and loops
def matrix_clockwise(mat):

    while mat:
        for x in mat.pop(0): # remove first row and print elements
            print(x)
        for v in mat: # remove last column and print elements
            print(v.pop())
        for x in mat.pop()[::-1]: # remove last row and print elements
            print(x)
        for v in mat[::-1]: # remove first column and print elements
            print(v.pop(0))
    

example_m = [   
                [1,  2,  3,  4,  5],
                [6,  7,  8,  9,  10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20]
            ]


print(matrix_clockwise(example_m))