# return index of two integers which add up to make the target value

def twoSum(nums, target):
    
    Hash = dict()
                
    for count, value in enumerate(nums):
        if target - value in Hash:
            return Hash[target - value], count
        else:
            Hash[value] = count

print(twoSum([2,7,11,15], 9))