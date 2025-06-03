# Exactly Three
# You are given a number n. Determine whether n has exactly 3 divisors or not.

# Examples
# is_exactly_three(4) ➞ True
# # 4 has only 3 divisors: 1, 2 and 4

# is_exactly_three(12) ➞ False
# # 12 has 6 divisors: 1, 2, 3, 4, 6, 12

# is_exactly_three(25) ➞ True
# # 25 has only 3 divisors: 1, 5, 25

# Notes
# 1 ≤ n ≤ 10^12

from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    
    if n <= 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    root = int(sqrt(n)) + 1
    for i in range(5, root, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    
    return True
    

def is_exactly_three(n):
    root = sqrt(n)
    if root.is_integer():
        return is_prime(root)
    
    return False


print(is_exactly_three(4), True)
print(is_exactly_three(12), False)
print(is_exactly_three(25), True)
print(is_exactly_three(121), True)
print(is_exactly_three(48), False)
print(is_exactly_three(1), False)
print(is_exactly_three(81), False)
print(is_exactly_three(1521), False)
print(is_exactly_three(225), False)
print(is_exactly_three(27550356289), True)
print(is_exactly_three(25235235235), False)
print(is_exactly_three(10), False)
print(is_exactly_three(64), False)
print(is_exactly_three(9), True)
print(is_exactly_three(144), False)
print(is_exactly_three(3), False)
print(is_exactly_three(2), False)
print(is_exactly_three(42351351), False)
print(is_exactly_three(999966000289), True)
print(is_exactly_three(20152357681), True)
print(is_exactly_three(531625249), True)
print(is_exactly_three(264306808866), False)
print(is_exactly_three(975179493674), False)
print(is_exactly_three(49), True)
print(is_exactly_three(165983), False)
