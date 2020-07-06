# Given a list of integers, return the largest product that can be made by multiplying any three integers.

# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

# You can assume the list has at least three integers.


# method
# loop through list
# multiply all elements with each other (product of 2 integers)
# store result in dict with index as key e.g. {1: [20, 5, 3], 2: [15, 6, 9], ...}
# create var largest_product
# loop through dict and multiply all values with ints in original list, skipping the element where index = key
# store largest product in largest_product and return
