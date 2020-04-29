# given a 32-bit signed integer, reverse digits of an integer e.g. 123 -> 321, -123 -> -321

def reverse(x):
    
    int_to_str = str(x)
    
    if x < 0:
        
        answer = int( int_to_str[::-1].strip("-") )
        answer = 0 - answer
    
    else:
        
        answer = int( int_to_str[::-1] )
        
    if (answer > 2**31 - 1) | (answer < -2**31):
        
        answer = 0

    return answer
        

print(reverse(321))
print(reverse(-321))