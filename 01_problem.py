'''
A. Love Story
time limit per test1 second
memory limit per test256 megabytes
Timur loves codeforces. That's why he has a string s
 having length 10
 made containing only lowercase Latin letters. Timur wants to know how many indices string s
 differs from the string "codeforces".

For example string s=
 "coolforsez" differs from "codeforces" in 4
 indices, shown in bold.

Help Timur by finding the number of indices where string s
 differs from "codeforces".

Note that you can't reorder the characters in the string s
.

Input
The first line contains a single integer t
 (1≤t≤1000
) — the number of test cases.

Each test case is one line and contains the string s
, consisting of exactly 10
 lowercase Latin characters.

Output
For each test case, output a single integer — the number of indices where string s
 differs.

Example
InputCopy
5
coolforsez
cadafurcie
codeforces
paiuforces
forcescode
OutputCopy
4
5
0
4
9

'''

for _ in range(int(input())):
    
    word = "codeforces"

    s = input()

    print(sum([ i != j  for i , j in zip(s, word)]))
