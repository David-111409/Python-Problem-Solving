"""
problem description:

The Kempner Function
The Kempner Function, applied to a composite number, permits to find the smallest integer greater than zero whose factorial is exactly divided by the number.

kempner(6) ➞ 3

1! = 1 % 6 > 0
2! = 2 % 6 > 0
3! = 6 % 6 === 0

kempner(10) ➞ 5

1! = 1 % 10 > 0
2! = 2 % 10 > 0
3! = 6 % 10 > 0
4! = 24 % 10 > 0
5! = 120 % 10 === 0
A Kempner Function applied to a prime will always return the prime itself.

kempner(2) ➞ 2
kempner(5) ➞ 5
Given an integer n, implement a Kempner Function.

Examples
kempner(6) ➞ 3
kempner(10) ➞ 5
kempner(2) ➞ 2
"""

from math import factorial

def kempner(n, k  = 1):
    if factorial(k) % n == 0:
        return k
    return kempner(n, k + 1)




print(kempner(6), 3, "Instructions: first example.")
print(kempner(10), 5, "Instructions: second example.")
print(kempner(2), 2, "Instructions: third example")
print(kempner(21), 7)
print(kempner(1), 1)
print(kempner(4), 4)
print(kempner(13), 13)
print(kempner(29), 29)
print(kempner(68), 17)
print(kempner(71), 71)
print(kempner(100), 10)
