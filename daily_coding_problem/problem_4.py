# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

def challenge(nums):

    nums_sorted = sorted(nums)
    prev_num = nums_sorted[0]
    answer = None

    for c,v in enumerate(nums_sorted[1:]):

        if v == prev_num + 1:
            prev_num = v
            pass
        else:
            answer = v+1
            break

    if answer == None:
        answer = nums_sorted[-1] + 1

    return answer

def challenge2(nums):

    if len(nums) == 0:
        answer = 1
        return answer

    Hash = {}
    smallest_num = nums[0]
    largest_num = nums[0]
    answer = None 

    for i in nums:
        Hash[i] = 1

        if i < smallest_num:
            smallest_num = i
        
        if i > largest_num:
            largest_num = i
            
    nums_corrected = list(range(smallest_num, largest_num+1))

    for j in nums_corrected:
        if j in Hash.keys():
            pass
        else:
            answer = j
            if answer == 0:
                answer = None
                pass
            else:
                break
    
    if answer == None:
        answer = nums_corrected[-1]+1

        while answer == 0:
            answer += 1

    return answer #Hash, answer
    

print(challenge2([3,4,-1,1]))
print(challenge2([1,2,0]))
print(challenge2([1, 2, 5]))
print(challenge2([1]))
print(challenge2([-1, -2]))
print(challenge2([]))
print(challenge2([-1, -2, 1]))

