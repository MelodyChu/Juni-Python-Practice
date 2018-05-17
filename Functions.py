"""
## write that takes in 2 numbers and returns their sum

def sum(a,b):
    return a + b
a = 1
b = 2
print (sum(a,b))

"""
## write a prime checker function returns T if prime and F if not prime


def prime_checker(a):
    if a == 1 or a == 0:
        return False
    for i in range(2,a):
        if a % i == 0:
            return False ## when do you need else?
    return True

#print (prime_checker(13))

def prime_printer(b):
    result = []
    for i in range(2,b):
        if prime_checker(i) == True:
            result.append(i)
    return result

print (prime_printer(500))
        
"""
## write a function that returns factorial of the inputted number

def factorial(b): # say b is 5
    result = 1
    for i in range(1,b+1): # b * (b-1) * (b-2)
        result *= i
    return result

print (factorial(5))
"""
"""
        
## write a function that returns the value of an exponent (function should take in base, power) do not use the Python ^ exponent 

def exponent(base,power):
    #result = base ** power
    return power

def exponent(base,power): ## if base=2 and power=3
    result = 1
    for i in range(1,power+1):
        return result *= base
    return result

print exponent(2,3)

"""
"""
print (exponent(2,3))

## use your prime_checker function to print all of the primes < 500

## want to loop through and print all primes up to 500
## interpreting as - for any a, print all prime #'s before it
def prime_checker(a):
    result = []
    if a == 1 or a == 0:
        return False ## not prime
    for i in range(2,a): # let's say a = 23, want [3,5,7,11, 13, 17...]
        if a % i == 0:
            return False ## a is not prime
        else:## if a is prime
            result.append(a) ## prime add to list
        return result

print (prime_checker(5))
   """

