# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

def largest_sum(l):

    inclusive = 0
    exclusive = 0

    for i in l:

        temp = inclusive

        inclusive = max(inclusive, exclusive + i)

        exclusive = temp

    answer = max(inclusive, exclusive)

    return answer
        
print(largest_sum([2, 4, 6, 2, 5]))
print(largest_sum([5, 1, 1, 20, 2]))
print(largest_sum([5, 1, 1, 5]))