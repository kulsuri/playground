# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
# e.g. [3, 0, 1] -> 2

def missingNumber(nums):

    Hash = dict()

    for c,v in enumerate(nums):
        Hash[v] = c
    
    for i in range(len(nums)+1):
        if i not in Hash:
            return i

    return None

print(missingNumber([3,0,1]))
print(missingNumber([9,6,4,2,3,5,7,0,1]))