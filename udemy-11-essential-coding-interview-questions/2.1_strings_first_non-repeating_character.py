# implement a function that takes a string and returns the first character that does not appeat twice or more in O(n) runtime

# Implement your function below.
def non_repeating(given_string):

    Hash = dict()

    for i in list(given_string):
        if i in Hash.keys():
            Hash[i] += 1
        else:
            Hash[i] = 1

    for i in list(given_string):
        if Hash[i] == 1:
            return i

    return None

# NOTE: The following input values will be used for testing your solution.
non_repeating("abcab") # should return 'c'
non_repeating("abab") # should return None
non_repeating("aabbbc") # should return 'c'
non_repeating("aabbdbc") # should return 'd'

print(non_repeating("abcab"))
print(non_repeating("abab"))
print(non_repeating("aabbbc"))
print(non_repeating("aabbdbc"))
