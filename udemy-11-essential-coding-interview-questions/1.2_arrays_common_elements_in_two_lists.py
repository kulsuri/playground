# return a list of common elements in two lists in O(n) runtime

# method 1
def common_elements(list1, list2):

    result = []

    # insert all elements of list1 into a hash table
    Hash = dict()
    for c,v in enumerate(list1):
        Hash[v] = 1
    
    # check if elements in list2 are in the hash table 
    for c,v in enumerate(list2):
        if v in Hash.keys():
            Hash[v] += 1

    # find elements in the hash table that have a value of 2
    for i in Hash:
        if Hash[i] == 2:
            result.append(i)
            
    return result

# method 2
def common_elements2(list1, list2):

    p1 = 0
    p2 = 0

    result = []

    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] == list2[p2]:
            result.append(list1[p1])
            p1 += 1
            p2 += 2
        elif list1[p1] > list2[p2]:
            p2 +=1
        else:
            p1 += 1

    return result

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

print(common_elements2(list_c1, list_c2))
