
'''
Recursion: Exact Factorial Bounds
Create a recursive function that tests if a number
is the exact upper bound of the factorial of n. 
If so, return a list that contains the exact factorial bound 
and n, or otherwise, the string "Not exact!".

Examples
is_exact(6) ➞ [6, 3]

is_exact(24) ➞ [24, 4]

is_exact(125) ➞ "Not exact!"

is_exact(720) ➞ [720, 6]

is_exact(1024) ➞ "Not exact!"

is_exact(40320) ➞ [40320, 8]
'''
def is_exact(n):
    
    def convert(n, fact = 2):
        if n == 1:
            return fact - 1
        
        elif n < 1:
            return 0
    
        return convert(n / fact, fact + 1)
    
    
    result = convert(n)
    return [n, result] if result else "Not exact!"


from inspect import getsource
from re import findall, MULTILINE

def check_recursive(fn):
  try:
    src, n = getsource(fn), fn.__name__
    if n == '<lambda>': n = src.split('=')[0].strip()
    return len(findall(n, src, flags=MULTILINE)) > 1
  except OSError: return True

for v in [True, False]:
  if v: print(check_recursive(is_exact), v)
  else: print(check_recursive(is_exact), v, 'Recursion is required!')

num_vectors, res_vectors = [
  2, 6, 24, 120, 5040, 40320, 3628800, 20922789888000, 
  125, 721, 1024, 41845579776000], [
  [2, 2], [6, 3], [24, 4], [120, 5], [5040, 7], [40320, 8], [3628800, 10], [20922789888000, 16],
  "Not exact!", "Not exact!", "Not exact!", "Not exact!"
] 

for i, n in enumerate(num_vectors):
  print(is_exact(n), res_vectors[i])
