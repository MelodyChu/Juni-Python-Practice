# Given a three-digit number, calculate the sum of its digits.

# For a given integer X, find the greatest integer n where 2^n is less than or equal to X.

def sum(digits):
    ones_digit = digits % 10 #gives me remainder of ones digit; 3 is remainder
    tens_digit = ((digits % 100) - ones_digit)/10 #gives me 23-3=20 but i want 2
    hundreds_digit = (digits - (tens_digit)*10 - ones_digit)/100 #new variable for hundreds digit
    return ones_digit + tens_digit + hundreds_digit
 

digits = 999
print (sum(digits))

# i realized i didn't need a loop for the above, after getting the error that digits is not iteratable

# 2nd question. Let's say X = 100, we want to find 2^n < 100
"""
def squares(integer):
    result = []
    for i in range(0,1000): #testing this; assuming no negative i's and 2^1000 seems pretty big to me..
        if 2 ** i <= integer:
            result.append(i) #so we'll have [0,1,2,3,4,5,6]
    for max in result:
        if max > i:
            max = i
    return max

integer = 10000
print (squares(integer)) """

import math
def squares(integer):
    i = integer
    while i > 0:
        logvar = math.log(i,2)
        if logvar % 1 == 0:
            return logvar
        i -= 1

integer = 100
print (squares(integer))
        
    
            
    
        

