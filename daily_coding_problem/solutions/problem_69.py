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

def max_product(ls):

    max_product_2_elements = dict()

    for k1,v1 in enumerate(ls):

        for k2,v2 in enumerate(ls):

            if k1 == k2:
                pass
            else:
                product = v1*v2
                index = (k1,k2)
                max_product_2_elements[index] = product

    largest_product = 0

    for i in max_product_2_elements:

        for k3,v3 in enumerate(ls):
            
            if k3 == i[0] or k3 == i[1]:
                pass
            elif max_product_2_elements[i] * v3 > largest_product:
                largest_product = max_product_2_elements[i] * v3
            else:
                pass

    return largest_product

list1 = [-10, -10, 5, 2]
list2 = [1, 1, 1]
list3 = [-5, -4, -3, 10, 10, 10]
print(max_product(list1))
print(max_product(list2))
print(max_product(list3))

