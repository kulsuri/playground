# linear search function
def linear_search(item_to_find, list_to_search):

    for i in list_to_search:
        if i == item_to_find:
            return list_to_search[ list_to_search.index(i) ]