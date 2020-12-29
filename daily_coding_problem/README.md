# daily-coding-problem
solutions to problems sent from:
https://www.dailycodingproblem.com/

# Pre-requisites
- python 3.6

# Installation Instructions
1. clone repo
```
git clone https://github.com/kulsuri/playground/tree/master/daily-coding-problem
```

# Problems

---

### Summary

No | Difficulty | File | Type
--- | --- | --- | ---
1 | Easy | [problem_1.py](solutions/problem_1.py) | arrays
2 | Hard | [problem_2.py](solutions/problem_2.py) | arrays
3 | Medium | [problem_3.py](solutions/problem_3.py) | tree
4 | Hard | [problem_4.py](solutions/problem_4.py) | arrays
5 | Medium | [problem_5.py](solutions/problem_5.py) | functions
6 | Hard | [problem_6.py](solutions/problem_6.py) | linked list
7 | Medium | [problem_7.py](solutions/problem_7.py) | strings
8 | Easy | [problem_8.py](solutions/problem_8.py) | trees
9 | Hard | [problem_9.py](solutions/problem_9.py) | arrays
10 | Medium | [problem_10.py](solutions/problem_10.py) | functions
11 | Medium | [problem_11.py](solutions/problem_11.py) | hash
12 | Hard | [problem_12.py](solutions/problem_12.py) | fibonacci
13 | Hard | [problem_13.py](solutions/problem_13.py) | strings
14 | Hard | [problem_14.py](solutions/problem_12.py) | tbc
15 | Hard | [problem_15.py](solutions/problem_12.py) | tbc
16 | Hard | [problem_16.py](solutions/problem_12.py) | tbc
 | | | 
55 | Easy | [problem_55.py](solutions/problem_55.py) | url shortener 
58 | Medium | [problem_58.py](solutions/problem_58.py) | lists 
63 | Easy | [problem_63.py](solutions/problem_63.py) | matrix
65 | Easy | [problem_65.py](solutions/problem_65.py) | matrix
66 | Medium | [problem_66.py](solutions/problem_66.py) | probability
69 | Easy | [problem_69.py](solutions/problem_69.py) | arrays
70 | Easy | [problem_70.py](solutions/problem_70.py) | integers
71 | Easy | [problem_71.py](solutions/problem_71.py) | functions

---

### Problem 1

Given a list of numbers, return whether any two sums to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

---

### Problem 2

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].

If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

---

### Problem 3

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

```
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

The following test should pass:
```
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'`
```

---


### Problem 4

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.

In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

---

### Problem 5

This problem was asked by Jane Street.

`cons(a, b)` constructs a pair, and `car(pair)` and `cdr(pair)` returns the first and last element of that pair.

For example, `car(cons(3, 4))` returns 3, and `cdr(cons(3, 4))` returns 4.

Given this implementation of cons:

```
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair`
```

---

### Problem 6

This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node.

Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

---

### Problem 7

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

Examples:

```
num_ways("3") = 1
```

```
num_ways("") = 1
```

```
num_ways("12345") = "a" + decode("2345) 
                    OR "l" + decode("345")
                    = num_ways("2345") + num_ways("345")
```

```
num_ways("27345") = "b" + decode("7345")
                    = num_ways("7345")
```

```
num_ways("011") = 0
```

---

### Problem 8

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

```
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
```

---

### Problem 9

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

---

### Problem 10

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

---

### Problem 11

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

---

### Problem 12

This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

- 1, 1, 1, 1
- 2, 1, 1
- 1, 2, 1
- 1, 1, 2
- 2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

---

### Problem 13

This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

---

---

### Problem 55

This problem was asked by Microsoft.

Implement a URL shortener with the following methods:

shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
Hint: What if we enter the same URL twice?

---

### Problem 58

This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.

---

### Problem 63

This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

```
[
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']
]
 ```

and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.

---

### Problem 65

This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

```
[
    [1,  2,  3,  4,  5],
    [6,  7,  8,  9,  10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]
```

You should print out the following:

```
1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
```

---

### Problem 66

This problem was asked by Square.

Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.

---

### Problem 69

This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.

---

### Problem 70

This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.

---

### Problem 71

This problem was asked by Two Sigma.

Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive).

---