# Task 1
#
# You are given a string.
# Your task is to find out if the string contains: alphanumeric characters, alphabetical characters,
#   digits, lowercase and uppercase characters.

def check_string(s):
    print( any(a.isalnum() for a in s))
    print( any(a.isalpha() for a in s))
    print( any(a.isdigit() for a in s))
    print( any(a.islower() for a in s))
    print( any(a.isupper() for a in s))



# Complex Pattern Print


thickness = int(input("Enter thickness: ")) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))



# Task
# Given 2 sets of integers, M and N, print their symmetric difference in ascending order.
# The term symmetric difference indicates those values that exist in either  M or N but do not exist in both.

M = int(input())
set1 = set(list(map(int,input().split())))

N = int(input())
set2 = set(list(map(int,input().split())))

set3 = sorted(set1.difference(set2).union(set2.difference(set1)))
for i in set3:
    print(i)



# Task : Count the number of most occuring letters.


a = 'szrmtbttyyaymadobvwniwmozojggfbtswdiocewnqsjrkimhovimghixqryqgzhgbakpncwupcadwvglmupbexijimonxdowqsjinqzytkooacwkchatuwpsoxwvgrrejkukcvyzbkfnzfvrthmtfvmbppkdebswfpspxnelhqnjlgntqzsprmhcnuomrvuyolvzlni'

from collections import Counter,OrderedDict

x = Counter(a)
res = {val[0] : val[1] for val in sorted(x.items(), key = lambda i: (-i[1], i[0]))}
p = Counter(res)
for i,j in p.most_common(3):
    print(i,j)


# Other solutions..

chars = Counter(input()).items()
for char, n in sorted(chars, key=lambda c: (-c[1], c[0]))[:3]:
    print(char, n)


# Other solutions..
class OrderedCounter(OrderedDict):
    pass

[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]



# Task : You are given a two lists A and B. Your task is to compute their cartesian product AxB.

from itertools import product

a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(product(a,b))
c.sort()
print(*c)