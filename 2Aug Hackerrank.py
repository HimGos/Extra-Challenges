# You have a non-empty set s, and you have to execute N commands given in N lines.
# The commands will be pop, remove and discard.
# Sample Input
#
# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop
# discard 6
# remove 5
# pop
# discard 5

n = int(input())
s = set(map(int, input().split()))
d = {'pop':s.pop, 'remove':s.remove, 'discard':s.discard}
N = int(input())
for _ in range(N):
    cmd = input().split()
    if len(cmd)>1:
        d[cmd[0]](int(cmd[1]))
    else:
        d[cmd[0]]()
print(sum(s))


"""" 
You are given a string S.
Your task is to find out whether S is a valid regex or not.

Input Format

The first line contains integer T, the number of test cases.
The next T lines contains the string S.

Sample input
    2
    .*\+
    .*+
""""

import re
T = int(input())
for _ in range(T):
    check =  True
    try:
        c = re.compile(input())
        print(check)
    except:
        check = False
        print(check)



"""
Validating Credit Card Number

► It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.

"""
import re

for _ in range(int(input())):
    s = input()

    if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", s) and not re.search(r"([\d])\1\1\1", s.replace('-', '')):
        print("valid")
    else:
        print('Invalid')
