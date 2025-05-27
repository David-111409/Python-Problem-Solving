
'''
Recursion: Halve and Halve Again
Given two integers a and b, 
return how many times a can be halved while still being greater than b.

Examples
halve_count(4666, 544) ➞ 3
# (4666 -> 2333 -> 1166.5 -> 583.25)

halve_count(624, 8) ➞ 6
# (624 -> 312 -> 156 -> 78 -> 39 -> 19.5 -> 9.75)

halve_count(1000, 3) ➞ 8
# (1000 -> 500 -> 250 -> 125 -> 62.5 -> 31.25 -> 15.625 -> 7.8125 -> 3.90625)

Notes
Integer a will always be (at least) greater than the twice of b.
You are expected to solve this challenge via a recursive approach.
'''


def halve_count(a, b):
    if a / 2 <= b:
        return 0
    
    return 1 + halve_count(a / 2, b)


from re import findall, MULTILINE
from inspect import getsource

def is_recursive(fn):
  try:
    src, n = getsource(fn), fn.__name__
    if n == '<lambda>': n = src.split('=')[0].strip()
    return len(findall(n, src, flags=MULTILINE)) > 1
  except OSError: return True

print(is_recursive(halve_count), False, 'Recursion is required!')

actual_param = [
  [4666, 544], [466, 54], [8, 2], [1891, 4], [1756, 14], [7764, 2], [1118, 47], [161, 79], [8573, 35], [4123, 1],
  [1348, 60], [7549, 31], [4469, 5], [1123, 98], [8197, 85], [1199, 56], [8845, 4], [606, 67], [3375, 6], [7085, 10],
  [299, 5], [1208, 82], [3635, 73], [2382, 3], [320, 80]
]
expected_param = [3, 3, 1, 8, 6, 11, 4, 1, 7, 12, 4, 7, 9, 3, 6, 4, 11, 3, 9, 9, 5, 3, 5, 9, 1]
for i, x in enumerate(actual_param): print(halve_count(*x), expected_param[i])
