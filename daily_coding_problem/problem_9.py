# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

def largest_sum(l):

    previous = 0 # 
    total = 0

    for i in l:
        
        previous, total = total, max(total, previous + i)

    return total

def largest_sum2(l):

    # loop through all elements in l
    # maintain two sums
    # prev_element_inc = max sum including the previous element
    # prev_element_exc = max sum excluding the previous element
    
    # max sum excluding the current element = max(prev_element_inc, prev_element_exc)
    # max sum including the current element = prev_element_exc + current element

    inc = 0
    exc = 0

    for i in l:

        # current max excluding i
        if exc > inc:
            new_exc = exc
        else:
            new_exc = inc

        
        # current max including i
        inc = exc + i
        exc = new_exc

    
    if exc > inc:
        return exc
    else:
        return inc
        
print(largest_sum([2, 4, 6, 2, 5]))
print(largest_sum([5, 1, 1, 20, 2]))

print(largest_sum2([2, 4, 6, 2, 5]))
print(largest_sum2([5, 1, 1, 20, 2]))
print(largest_sum2([5, 1, 1, 5]))