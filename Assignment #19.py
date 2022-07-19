# 1. Narcissistic Number :-

def narcissistic(value):
    return True if value == sum([int(i)**len(str(value)) for i in str(value)]) else False


print(narcissistic(371))


# 2. Complete the method/function so that it converts dash/underscore delimited words into camel casing.
#    The first word within the output should be capitalized only if the original word was
#    capitalized (known as Upper Camel Case, also often referred to as Pascal case).


# MY METHOD

import re

check = re.sub('[_-]', " ", "The-Stealth-Warrior")
print(check.split()[0] + ''.join(check.title().split()[1:]))


# Better method

def to_camel_case(text):
    return re.sub('[_-](..)', lambda x: x.group(1).upper(), text)

print(to_camel_case("The-Stealth-Warrior"))


# 3. Write an algorithm that takes an array and moves all of the zeros to the end,
#   preserving the order of the other elements.


# MY METHOD

def move_zeros(lst):
    for _ in range(lst.count(0)):
        lst.append(0)
        lst.pop(lst.index(0))
    return lst

