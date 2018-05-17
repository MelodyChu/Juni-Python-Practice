# function that takes in a list of numbers and return a list of numbers that occurs most frequently
# [1,1,2,2,3,3,4] return [1,2,3]
"""
firstlist = [1,1,1,2,2,3,3,4]

def frequency(firstlist):
    dict1 = {}
    maxval = 0
    finallist = []
    for number in firstlist:
        if number in dict1:
            dict1[number] += 1
        else:
            dict1[number] = 1 #should give dictionary where keys are numbers and values are frequencies of those numbers
    #return (dict1)
    #print (dict1)
    for key in dict1:
        if dict1[key] > maxval: #if value in dictioary > maxval
            maxval = dict1[key] # set maxval = to dict1 to find greatest maxval
    for key in dict1:
        if dict1[key] == maxval:
            finallist.append(key)
        #finallist.append(dict1.index[maxval]) # how to return this into a list?
    return (finallist)
print (frequency(firstlist))
"""

# Codeacademy practice
# 3
"""
x = 2.5
def is_int(x):
  if abs(x) == abs(min(x)):
    print ('True')
  else:
    print ('False')
return is_int(x)
"""

#4 - how to write this as a loop? -- review
"""
n = 1234
sum1 = 0
while n != 0:
    sum1 += (n % 10)
    n = (n - (n % 10))/10 # turn into 123
print (sum1)
"""
 

"""
def digit_sum(n):
    ones_digit = n % 10 # 1234/10 = 123 remainder 4
    tens_digit = ((n - ones_digit) % 100)/10 # 1234-4 = 1230. 1230 / 100 = 12 remainder 30
    hundreds_digit = ((n - (tens_digit*10) - ones_digit) % 1000)/100 # 1234 - 30 - 4 = 1200; 1200/1000 = 1 remainder 200
    thousands_digit = ((n - (hundreds_digit*100) - (tens_digit*10) - ones_digit) % 10000)/1000
    sum1 = (thousands_digit + hundreds_digit + tens_digit + ones_digit)
    return sum1
print (digit_sum(n))
"""

#5 - factorials 
"""
x = 7
def factorial(x):
    result = 1
    n = 0 # use to iterate through decreasing numbers by 1
    while x > 1 and n < x: # let's assume x = 4, 0 is <4; you want 4 * 3 * 2 * 1
        result *= x-n # first time result *= 4 so result = 4. 2nd time: result = 4*3, but n will tur
        n += 1
    return (result)
print (factorial(x))
        
"""
"""
#6 - is (come back to this prime # question)

x = 10
def is_prime(x):
    n = 1
    while x > 2 and n < x: #if x = 5
        if x % (x-n) == 0:
            n += 1
            print ('False')
        else: 
            print ('True')
    return # where to put this without returning function too early
print (is_prime(x))
        
"""


            
 
    
