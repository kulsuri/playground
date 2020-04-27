# implement a function that assigns correct numbers ina field of minesweeper


def mine_sweeper(bombs, num_rows, num_cols):
    # NOTE: field = [[0] * num_cols] * num_rows would not work
    # because you need to create a new list for every row,
    # instead of copying the same list.

    # create map
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]

    # update bomb positions
    for i in bombs:
        row = i[0]
        col = i[1]

        field[row][col] = -1

        # update bomb 8 surrounding positions
        
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
            # check if position is not an existing bomb position
            elif field[ position[0] ][ position[1] ] == -1:
                pass
            else:
                field[ position[0] ][ position[1] ] += 1
    
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
# mine_sweeper([[0, 2], [2, 0]], 3, 3) should return:
# [[0, 1, -1],
#  [1, 2, 1],
#  [-1, 1, 0]]

# mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4) should return:
# [[-1, -1, 2, 1],
#  [2, 3, -1, 1],
#  [0, 1, 1, 1]]

# mine_sweeper([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5) should return:
# [[1, 2, 2, 1, 0],
#  [1, -1, -1, 2, 0],
#  [1, 3, -1, 2, 0],
#  [0, 1, 2, 2, 1],
#  [0, 0, 1, -1, 1]]


print(to_string(mine_sweeper([[0, 2], [2, 0]], 3, 3)))
print(to_string(mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4)))
print(to_string(mine_sweeper([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5)))