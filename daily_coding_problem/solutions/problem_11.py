# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

# For example, given the query string 'de' and the set of strings [dog, deer, deal], return [deer, deal].

# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

def get_autocomplete_suggestions(s, query_strings):

    Hash = dict()

    for i in query_strings:
        if i[:2] in Hash:

            Hash[ i[:2] ].append(i)
        else:
            Hash[ i[:2] ] = [i]

    if s not in Hash:
        answer = []
    else:
        answer = Hash[s]
    
    return answer



print(get_autocomplete_suggestions("de", ["dog", "deer", "deal"]))
assert get_autocomplete_suggestions("de", ["dog", "deer", "deal"]) == ["deer", "deal"]
assert get_autocomplete_suggestions("ca", ["cat", "car", "cer"]) == ["cat", "car"]
assert get_autocomplete_suggestions("ae", ["cat", "car", "cer"]) == []
assert get_autocomplete_suggestions("ae", []) == []