# write a fn that sums the first n numbers; n is input

"""
def sumn(n):
    result = 0
    for i in range(0,n+1):
        result += i
    return result

print (sumn(n))
"""
"""
n = 5
def sumn(n):
    if n == 1:
        return 1
    return n + sumn(n-1)
print (sumn(n))
"""
"""
n = 5
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print (factorial(n))
"""
"""
base = 3
power = 2
def exponent(base, power):
    if power == 0:
        return 1
    return base * exponent(base,power - 1)
print (exponent(4,3))
"""

# Write a recursive function that takes in a number N and returns the nth Fibonacci number.
# 0, 1, 1, 2, 3, 5, 8...
# Hint: You can try writing the solution iteratively first.
# if we input 5, return 5th number (which is 3)
n = 6
def recursion(n):
    result = 0 # placeholder
    prior1 = 1
    prior2 = 0 # to take the place of prior1
    for i in range(0,n): #iterates through indexes up to n
        if i == 0:
            result = 0
        #elif i == 1:
            #result = 1
        elif i > 0:
            result = prior1 + prior2 #so if i = 2, prior1 = 1 and prior2 = 0, so result = 1
            prior2 = prior1
            prior1 = result
    return result

print (recursion(n))

"""
# writing recursion..
# 0, 1, 1, 2, 3, 5, 8...
n = 6 #whatever user input is
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)
print (fib(n))
"""












