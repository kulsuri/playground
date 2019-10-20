# unordered list of elements
unordered_list = [99, 47, 63, 29, 16, 7, 92, 53, 39, 28, 1, 81, 69, 72]

# linear search function
def linear_search(item_to_find, list_to_search):

    for i in list_to_search:
        if i == item_to_find:
            return i, list_to_search.index(i)

# call the linear search function, searching for the element 1
a, b = linear_search(1, unordered_list)
print("element", a, "found at index position", b)