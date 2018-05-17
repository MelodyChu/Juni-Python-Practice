def sum(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n + sum(n-1)

n = 5
print (sum(n))

# factorial function; calculate factorial of number

def factorial(x):
    if x == 0:
        return 1
    if x == 1:
        return 1
    return x * factorial(x-1)

x = 5
print (factorial(5))

# function that takes in a base and exponent and calculates value of base to that exponent

def exponent(y,z):
    if z == 0: # base case purpose: at one point, the function needs to stop
        return 1
    return y * exponent(y,z-1)

y = 10
z = 3
print (exponent(y,z))

# function that takes in a number and return the sum of its digits (think about recursive case)
# let's say number is 123
def sumdigits(b):
    if b == 0:
        return 0
    d = b%10 #gets the ones digit of number
    return d + sumdigits((b-d)/10)

b = 525
print (sumdigits(b))

def sumdigits(b):
    sum = 0
    while b >= 0:
        sum += b % 10
        b = (b-b%10)/10

    
    
