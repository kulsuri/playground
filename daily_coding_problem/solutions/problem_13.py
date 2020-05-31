# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


def longest_substring(k, s):

    # distinct_char_count = k

    stack = []
    Hash = dict()
    count = 0

    for y in range(len(s)):

        distinct_char_count = k

        for i in s[y:]:

            if count not in Hash:
                Hash[count] = [i]
                distinct_char_count = distinct_char_count - 1
            
            elif i in Hash[count]:

                Hash[count].append(i)
                #stack.append(i)

            elif distinct_char_count > 0:

                distinct_char_count = distinct_char_count - 1

                Hash[count].append(i)
                #stack.append(i)
            
            else:
                
                count += 1
                break

    return Hash


print(longest_substring(2, "abcba"))