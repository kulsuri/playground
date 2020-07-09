# A number is considered perfect if its digits sum up to exactly 10.

# Given a positive integer n, return the n-th perfect number.

# For example, given 1, you should return 19. Given 2, you should return 28.

def perfect_number(num):

    temp_sum = 0

    for i in str(num):

        temp_sum += int(i)

    perfect_num = (num * 10) + (10 - temp_sum)

    return perfect_num


print(perfect_number(1))
print(perfect_number(2))
print(perfect_number(10))
print(perfect_number(11))
print(perfect_number(19))

assert perfect_number(1) == 19
assert perfect_number(2) == 28
assert perfect_number(3) == 37
assert perfect_number(10) == 109
assert perfect_number(11) == 118
assert perfect_number(19) == 190