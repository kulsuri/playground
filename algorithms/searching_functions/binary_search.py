# binary search function
def binary_search(list_to_search, element_to_find, starting_position = 0, closing_postion = None):

    # define the closing position for first iteration of search
    if closing_postion == None:
        closing_postion = len(list_to_search) - 1

    # return False is the element does not exist
    if starting_position > closing_postion:
        return False

    # define middle position
    mid_position = (starting_position + closing_postion) // 2

    # check that the element to find does not occur in the middle of the list
    if element_to_find == list_to_search[mid_position]:
        return list_to_search[mid_position]

    # if the element to find is smaller than the middle position, then the closing position now becomes the middle position
    if element_to_find < list_to_search[mid_position]:
        return binary_search(list_to_search, element_to_find, starting_position, mid_position - 1)
    
    # if the element to find is larger than the middle position, then the starting position now becomes the middle position
    else:
        return binary_search(list_to_search, element_to_find, mid_position + 1, closing_postion)