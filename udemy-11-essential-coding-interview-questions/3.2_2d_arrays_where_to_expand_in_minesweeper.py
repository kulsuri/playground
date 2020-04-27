# implement a function that turns revealed cells into 02 given a location the user wants to click

def click(field, num_rows, num_cols, given_i, given_j):

    if field[given_i][given_j] != 0:
        return field
    else:
        return modify_field(field, num_rows, num_cols, given_i, given_j)
    
def modify_field(field, num_rows, num_cols, given_i, given_j):

    row = given_i
    col = given_j
    
    p1 = [row-1, col-1]    # top left 
    p2 = [row-1, col]      # above 
    p3 = [row-1, col+1]    # top right
    p4 = [row, col-1]      # left
    p5 = [row, col+1]      # right
    p6 = [row+1, col-1]    # bottom left 
    p7 = [row+1, col]      # below
    p8 = [row+1, col+1]    # bottom right

    positions = [p1, p2, p3, p4, p5, p6, p7, p8]
    
    for position in positions:
        
        # check if position is in bounds of field
        if position[0] < 0 or position[0] > len(field)-1 or position[1] < 0 or position[1] > len(field[0])-1:
            pass
        # check if position is a non-zero value
        elif field[ position[0] ][ position[1] ] != 0:
            pass
        else:
            field[ position[0] ][ position[1] ] += -2
            modify_field(field, num_rows, num_cols, position[0], position[1])

    return field


# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


# NOTE: The following input values will be used for testing your solution.
field1 = [[0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 1, -1, 1, 0]]

# click(field1, 3, 5, 2, 2) should return:
# [[0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 0],
#  [0, 1, -1, 1, 0]]

# click(field1, 3, 5, 1, 4) should return:
# [[-2, -2, -2, -2, -2],
#  [-2, 1, 1, 1, -2],
#  [-2, 1, -1, 1, -2]]


field2 = [[-1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, -1]]

# click(field2, 4, 4, 0, 1) should return:
# [[-1, 1, 0, 0],
#  [1, 1, 0, 0],
#  [0, 0, 1, 1],
#  [0, 0, 1, -1]]

# click(field2, 4, 4, 1, 3) should return:
# [[-1, 1, -2, -2],
#  [1, 1, -2, -2],
#  [-2, -2, 1, 1],
#  [-2, -2, 1, -1]]

print(to_string(click(field1, 3, 5, 2, 2)))
print(to_string(click(field1, 3, 5, 1, 4)))
print(to_string(click(field2, 4, 4, 0, 1)))
print(to_string(click(field2, 4, 4, 1, 3)))