# https://medium.com/@amirziai/merge-sort-walkthrough-with-code-in-python-e4f76d90a4ea
# step 1: given a list, split the list down the middle
def merge_sort_split_list(list_to_sort):

    midpoint = len(list_to_sort) // 2
    left_half = list_to_sort[:midpoint]
    right_half = list_to_sort[midpoint:]

    return left_half, right_half

# step 2: given two sorted lists, merge them into a single list
def merge_sort_merge_sorted_list(list_left, list_right):

    # special case: if one or both lists are empty
    if len(list_left) == 0:
        return list_right
    elif len(list_right) == 0:
        return list_left

    # general case
    index_left = index_right = 0
    list_merged = [] # list to build and return
    list_len_target = len(list_left) + len(list_right)

    while len(list_merged) < list_len_target:
        
        if list_left[ index_left ] <= list_right[ index_right ]:
            # value on the left list is smaller (or equal) so it should be selected
            list_merged.append( list_left[ index_left ] )
            index_left += 1
        
        else:
            # value on the right list is smaller (or equal) so it should be selected
            list_merged.append( list_right[ index_right ] )
            index_right += 1

        # if we are at the end of one of the lists we can take a shortcut
        if index_right == len( list_right ):
            # reached end of right list
            # append the remaining elements of the left list and break
            list_merged += list_left[ index_left: ]
            break
        elif index_left == len(list_left):
            # reached end of left list
            # append the remaining elements of the right list and break
            list_merged += list_right [ index_right: ]
            break

    return list_merged

# step 3: merge sort function
def merge_sort(list_to_sort):
    # only needs to utilize split_list and merge_sorted_list
    # need to split the lists until they have a single element
    # a list with a single element is sorted
    # then we can merge these single-element (or empty) lists

    if len(list_to_sort) <= 1:
        return list_to_sort
    else:
        left, right = merge_sort_split_list( list_to_sort )
        return merge_sort_merge_sorted_list( merge_sort( left ), merge_sort( right ) )
