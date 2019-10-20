# unordered list of elements
list_of_items = [99, 47, 63, 29, 16, 7, 92, 53, 39, 28, 1, 81, 69, 72]

# linear search function
def linear_search(item_to_find, list_to_search):

    for i in list_of_items:
        if i == item_to_find:
            return print(i)

linear_search(1, list_of_items)