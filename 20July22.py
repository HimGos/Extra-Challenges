# 1. Build a pyramid-shaped tower given a positive integer number of floors.
#    A tower block is represented with "*" character.

def tower_builder(n):
    return [(('*'*(i*2-1)).center(n*2-1)) for i in range(1,n+1)]


print(tower_builder(3))


# 2. In this kata you have to create all permutations of a non empty input string and remove duplicates, if present.
#    This means, you have to shuffle all letters from the input in all possible orders.

from itertools import permutations as p


def permutations(s):
    return list(set([''.join(i) for i in p(s)]))

print(permutations('aabb'))


# 3. REGEX Password validation...

from re import compile, VERBOSE

regex = compile("""
^              # begin word
(?=.*?[a-z])   # at least one lowercase letter
(?=.*?[A-Z])   # at least one uppercase letter
(?=.*?[0-9])   # at least one number
[A-Za-z\d]     # only alphanumeric
{6,}           # at least 6 characters long
$              # end word
""", VERBOSE)