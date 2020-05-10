def is_char(code):
    if 1 <= int(code) <= 26:
        return 1
    else:
        return 0

def get_message_count(code):

    if len(code) == 1:
        count = 1
    elif len(code) == 2:
        count = 1 + is_char(code)
    else:
        count = get_message_count( code[1:] )

        if is_char( code[:2] ):
            count += get_message_count( code[2:] )
    
    return count


print(get_message_count("123"))