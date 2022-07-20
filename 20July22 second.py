# 1. Checking Valid parantheses.

def valid_parentheses(string):
    count = 0
    for i in string:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0

print(valid_parentheses('((((()))))'))


# 2. Define a function that takes in two non-negative integers a and b and returns the
#    last decimal digit of a^b. Note that a and b may be very large!
#
# For example, the last decimal digit of 9^7 is 9, since 9^7= 47829699

def last_digit(n1,n2):
    return pow(n1,n2,10)

print(last_digit(2**200, 2**300))


# 3. Simple Pig Latin

def pig_it(text):
    return " ".join([i[1:] + i[0] + 'ay' if i.isalnum() else i for i in text.split()])

print(pig_it("Hello This is , test program !"))