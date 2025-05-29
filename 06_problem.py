'''
Can You Make the Numbers?
You are given a list representing the number of 0s, 1s, 2s, ..., 9s you have. 
The function will look like:

can_build([#0s, #1s, #2s, ..., #9s], [num1, num2, ...])
Write a function that returns True if you can build the following numbers using only the digits you have.

Examples
can_build([0, 1, 2, 2, 3, 0, 0, 0, 1, 1], [123, 444, 92]) ➞ True

# You have: one 1, two 2s, two 3s, three 4s, one 8 and one 9
# Using only these digits, you can build 123, 444, and 92

can_build([10, 2, 3, 8, 5, 8, 5, 5, 3, 1], [11, 2, 22, 49, 444, 998, 87, 44]) ➞ False

can_build([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], []) ➞ True

can_build([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [3]) ➞ False
'''

def can_build(allowed_numbers, numbers):
    
    whole_numbers = ''.join(map(str, numbers))
    
    counts = [ whole_numbers.count(f'{i}') for i in range(10) ]
    
    return all([ m <= n for m, n in zip(counts , allowed_numbers)])



print(can_build([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], []), True)
print(can_build([1, 1, 0, 0, 0, 0, 0, 0, 1, 0], [1, 8]), True)
print(can_build([1, 1, 0, 0, 0, 0, 0, 0, 1, 0], [1, 80]), True)
print(can_build([0, 1, 2, 2, 3, 0, 0, 0, 1, 1], [123, 444, 92]), True)
print(can_build([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [10, 23, 45, 6789]), True)
print(can_build([0, 2, 3, 0, 5, 0, 0, 0, 0, 1], [11, 2, 22, 49, 444, 4]), True)
print(can_build([1, 1, 0, 0, 0, 0, 0, 0, 1, 0], [1, 80, 0]), False)
print(can_build([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1]), False)
print(can_build([0, 2, 3, 0, 5, 0, 0, 0, 0, 1], [11, 7, 2, 22, 49, 444, 4]), False)
print(can_build([0, 2, 3, 0, 5, 0, 0, 0, 0, 1], [11, 2, 22, 49, 444, 44]), False)
print(can_build([10, 2, 3, 8, 5, 8, 5, 5, 3, 1], [11, 2, 22, 49, 444, 998, 87, 44]), False)
