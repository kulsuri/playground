# return a list of common elements in two lists in O(n) runtime

def common_elements(list1, list2):

    result = []

    Hash = dict()

    for c,v in enumerate(list1):
        Hash[v] = 1
    
    for c,v in enumerate(list2):
        if v in Hash.keys():
            Hash[v] += 1

    for i in Hash:
        if Hash[i] == 2:
            result.append(i)
            
    return print(result)


# NOTE: The following input values will be used for testing your solution.
list_a1 = [1, 3, 4, 6, 7, 9]
list_a2 = [1, 2, 4, 5, 9, 10]
# common_elements(list_a1, list_a2) should return [1, 4, 9] (a list).

list_b1 = [1, 2, 9, 10, 11, 12]
list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
# common_elements(list_b1, list_b2) should return [1, 2, 9, 10, 12] (a list).

list_c1 = [0, 1, 2, 3, 4, 5]
list_c2 = [6, 7, 8, 9, 10, 11]
# common_elements(list_b1, list_b2) should return [] (an empty list).

common_elements(list_c1, list_c2)
