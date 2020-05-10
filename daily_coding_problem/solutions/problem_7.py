# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.

# '1111' = 5, as 'aaaa', 'kaa', 'aka', 'aak', 'kk'

# 2 base cases:

# (1) when string is empty 
# (2) string starts with a 0

# 2 recursive cases:

# (1) call function recursively twice e.g. "12345" -> "2345" + "345"
# (2) call function recursively once e.g. "27345" -> "7345"

def helper(data, k):

    # num_ways("") = 1
    if k == 0:
        return 1
    
    # num_ways("011") = 0
    starting_index = len(data) - k
    if data[starting_index] == "0":
        return 0
    
    # num_ways("27345", k) = helper("27345", k-1)
    result = helper(data, k-1)

    # num_ways("12345", k) = helper("12345", k-1) + helper("12345", k-2)
    if 2 <= k and int(data[starting_index:starting_index+2]) <= 26:
        result += helper(data, k-2)
    
    return result


def num_ways(data):

    return helper(data, len(data))
    

print(num_ways("1111"))



    




