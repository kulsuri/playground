# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 

# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

def challenge(nums):

    total = 1
    answer = []

    for i in nums:

        total *= i

    for i in nums:
        
        product_exc_index = int(total / i)

        answer.append(product_exc_index)

    return answer

def challenge_without_division(nums):

    answer = []

    for c1,v1 in enumerate(nums):
        
        total = 1
        
        for c2,v2 in enumerate(nums):

            if c1 == c2:
                pass
            else:
                total *= v2

        answer.append(total)
    
    return answer

         

            

print(challenge([3,2,1]))
print(challenge([1,2,3,4,5]))

print(challenge_without_division([3,2,1]))
print(challenge_without_division([1,2,3,4,5]))

