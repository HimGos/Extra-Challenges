# Designing Door Mat --- String Pattern
# Enter 2 values , second one should be triple of first one. eg,  7 21 , 10,30

n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))



# Given an integer, n, print the following values for each integer from to :
#
# 1. Decimal
# 2. Octal
# 3. Hexadecimal (capitalized)
# 4. Binary

# The four values must be printed on a single line in the order specified above for each i from 1 to number.
# Each value should be space-padded to match the width of the binary value of number and
# the values should be separated by a single space.


def print_formatted(number):
    w = len(bin(number)[2:])
    for i in range(1,number+1):
        print(f"{str(i).rjust(w,' ')} {str(oct(i))[2:].rjust(w,' ')} "
              f"{str(hex(i))[2:].upper().rjust(w,' ')} {str(bin(i))[2:].rjust(w,' ')}",sep=" ")



# You are given a date. Your task is to find what the day is on that date.

import pandas as pd

date = input("Enter Date in DD MM YYYY format: ")
day = pd.Timestamp('{}-{}-{}'.format(date[6:],date[3:5],date[:2]))
print(day.day_name())

#-------

import calendar

n1,n2,n3=map(int,input().split())
print((calendar.day_name[calendar.weekday(n3,n1,n2)]).upper())



# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

def diagonalDifference(arr):
    a = sum([arr[i][i] for i in range(len(arr))])
    b = sum([arr[i][len(arr) - i - 1] for i in range(len(arr))])

    return abs(a - b)
