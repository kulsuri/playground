# determine if input string is valid

def isValid(s):

    s = list(s)

    round_b = ('(', ')')
    curly_b = ('{', '}')
    square_b = ('[', ']')

    to_be_closed = []

    for i in s:

        if i == round_b[0] or i == curly_b[0] or i == square_b[0]:
            to_be_closed.append(i)
        
        else:
            if len(to_be_closed) == 0:
                return False
            else:
                item_to_close = to_be_closed[-1]

            if item_to_close == round_b[0] and i == round_b[1]:
                to_be_closed.pop()
            elif item_to_close == curly_b[0] and i == curly_b[1]:
                to_be_closed.pop()
            elif item_to_close == square_b[0] and i == square_b[1]:
                to_be_closed.pop()
            else:
                return False

    if len(to_be_closed) == 0:
        return True
    else:
        return False
    


print(isValid("()[]{}"))
print(isValid("()"))
print(isValid("(]"))
print(isValid("([)]"))
print(isValid("{[]}"))
print(isValid("["))
print(isValid("}"))
print(isValid(""))



