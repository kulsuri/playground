# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

# get positive integer subset
def get_positive_subset(nums):
    positive_nums = []
    for i in nums:
        if i <= 0:
            pass
        else:
            positive_nums.append(i)
    return positive_nums

def challenge(nums):

    nums = get_positive_subset(nums)
    # if empty list then return lowest positive integer = 1
    if len(nums) == 0:
        answer = 1
        return answer

    Hash = {} # empty dict
    smallest_num = nums[0] # store smallest int
    largest_num = nums[0] # store largest int
    answer = None # store answer for first missing positive integer

    # loop through list, store value in dictionary and determine smallest and largest integer
    for i in nums:
        Hash[i] = 1

        if i < smallest_num:
            smallest_num = i
        
        if i > largest_num:
            largest_num = i
    
    # create new correct and complate list based on smallest_num and largest_num
    nums_corrected = list(range(smallest_num, largest_num+1))

    # compare initial list nums with correct list nums_corrected
    for j in nums_corrected:
        if j in Hash.keys(): # check if element is in dictionary
            pass
        else:
            answer = j # if number is not in dictionary then answer = j
            if answer == 0: # check if answer does not equal zero
                answer = None # reset answer back to zero and continue loop
                pass
            else: # otherwise answer has been found and break
                break
    
    if answer == None: # if answer is None that means that nums was not missing an element in the middle 
        answer = nums_corrected[-1]+1 # so missing element is at the end

        while answer == 0: # answer cannot be zero
            answer += 1

    return answer
    

print(challenge([3,4,-1,1]))
print(challenge([1,2,0]))
print(challenge([1, 2, 5]))
print(challenge([1]))
print(challenge([-1, -2]))
print(challenge([]))
print(challenge([-1, -2, 1]))
print(challenge([-2, -3, -5, -4]))

