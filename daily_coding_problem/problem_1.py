# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

def challenge(nums, k):

    Hash = {}

    for c,v in enumerate(nums):
        if k-v in Hash:
            return v, k-v
        else:
            Hash[v] = c

print(challenge([10, 15, 3, 7], 17))

