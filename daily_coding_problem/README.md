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

## Problem 1

---


No | Difficulty | File | Objective
--- | --- | --- | ---
1 | Easy | [problem_1.py](problem_1.py) | Given a list of numbers, return whether any two sums to k.<br><br>For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.<br><br>Bonus: Can you do this in one pass?
2 | Hard | [problem_2.py](problem_2.py) | This problem was asked by Uber.<br><br>Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.<br><br>For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].<br><br>If our input was [3, 2, 1], the expected output would be [2, 3, 6].<br><br>Follow-up: what if you can't use division?
3 | Medium | [problem_3.py](problem_3.py) | This problem was asked by Google.<br><br>Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.<br><br>For example, given the following Node class<br><br>`class Node:`<br>   `def __init__(self, val, left=None, right=None):`<br>       `self.val = val`<br>        `self.left = left`<br>      `self.right = right`<br><br>The following test should pass:<br><br>`node = Node('root', Node('left', Node('left.left')), Node('right'))`<br>`assert deserialize(serialize(node)).left.left.val == 'left.left'`
4 | Hard | [problem_4.py](problem_4.py) | This problem was asked by Stripe.<br><br>Given an array of integers, find the first missing positive integer in linear time and constant space.<br><br>In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.<br><br>For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.<br><br>You can modify the input array in-place.
5 | Medium | [problem_5.py](problem_5.py) | This problem was asked by Jane Street.<br><br>`cons(a, b)` constructs a pair, and `car(pair)` and `cdr(pair)` returns the first and last element of that pair.<br><br>For example, `car(cons(3, 4))` returns 3, and `cdr(cons(3, 4))` returns 4.<br><br>Given this implementation of cons:<br><br>`def cons(a, b):`<br>`def pair(f):`<br>`return f(a, b)`<br>`return pair`
6 | Hard | [problem_6.py](problem_6.py) | This problem was asked by Google.<br><br>An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node.<br><br>Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.<br><br>If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
7 | Medium | [problem_7.py](problem_7.py) | This problem was asked by Facebook.<br><br>Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.<br><br>For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.<br><br>You can assume that the messages are decodable. For example, '001' is not allowed.
8 | Easy | [problem_8.py](problem_8.py) | This problem was asked by Google.<br><br>A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.<br><br>Given the root to a binary tree, count the number of unival subtrees.<br><br>For example, the following tree has 5 unival subtrees:<br><br>


