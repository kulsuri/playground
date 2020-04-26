# return the most frequent element in an array in O(n) runtime

def most_frequent(given_array):

    # insert all elements and corresponding count in a hash table
    Hash = dict()
    for c,v in enumerate(given_array):
        if given_array[c] in Hash.keys():
            Hash[given_array[c]] += 1
        else:
            Hash[given_array[c]] = 1
    
    # find the max frequency
    max_count = 0
    result = None
    for i in Hash:
        if max_count < Hash[i]:
            result = i
            max_count = Hash[i]

    return print(result)


# Examples

# most_frequent(list1) should return 1
list1 = [1, 3, 1, 3, 2, 1]
# most_frequent(list2) should return 3
list2 = [3, 3, 1, 3, 2, 1]
# most_frequent(list3) should return None
list3 = []
# most_frequent(list4) should return 0
list4 = [0]
# most_frequent(list5) should return -1
list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]

most_frequent(list1)