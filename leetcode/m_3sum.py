# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero

def threeSum(nums):

    Hash = dict()
    solution = []

    for c1,v1 in enumerate(nums):
        for c2,v2 in enumerate(nums[c1+1:]):
            c = -v1-v2
            Hash[c] = v1,v2

    print(Hash)
    for i in nums:
        if i in Hash:
            solution.append( [ i, Hash[i][0], Hash[i][1] ] )

    #sol2 = set(solution)
    return solution



print(threeSum([-1,0,1,2,-1,-4]))