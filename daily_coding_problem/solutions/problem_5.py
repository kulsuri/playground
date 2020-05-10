# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 

# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons, implement car and cdr.

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# calling cons(a, b) returns a new function object; the pair(f) function inside of cons(a,b)
# the pair(f) function returns a new function object; f(a, b)
# cons() creates an inner function pair(), and pair() has access to the parameters a and b via its closure

# cons(a, b) -> pair(f) -> f(a, b)
# car( cons(a, b) ) = car( pair(f) ) = car( f(a,b) )
# car() must create a function to pass to pair() that will extract a
# car( pair_s ) = car( f(a,b) )
# pair_s(return_first) = f(a,b)

def car(pair_s):

    def return_first(a,b):
        return a
    return pair_s(return_first)


def cdr(pair_s):

    def return_last(a,b):
        return b
    return pair_s(return_last)

def return_first(a,b):
    return a

print(cons(3,4)(return_first))

print(car(cons(3,4)))
print(cdr(cons(3,4)))