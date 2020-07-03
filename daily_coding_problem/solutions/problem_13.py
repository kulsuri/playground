# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


def longest_substring(k, s):

    Hash2 = dict()

    for y,v in enumerate(s):

        distinct_char_count = k

        for i in s[y:]:

            if y not in Hash2:

                Hash2[y] = [i]
                distinct_char_count = distinct_char_count - 1
            
            elif i in Hash2[y]:

                Hash2[y].append(i)

            elif distinct_char_count > 0:

                distinct_char_count = distinct_char_count - 1
                Hash2[y].append(i)
            
            else:
                
                break

    ans = Hash2[0]
    for i in Hash2:

        if len(Hash2[i]) > len(ans):
            ans = Hash2[i]   
        
    return ans

print(longest_substring(2, "abcba"))