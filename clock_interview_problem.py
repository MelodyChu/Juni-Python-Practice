# write a function that takes in two numbers,
# the hour and the minute of a time,
# and returns the angle between the 12 on the clock and the hour hand,
# measured clockwise from the 12

hour = 12 # as example; between 1 and 12
minute = 59 # as example; between 1 and 60
# exception - when hour is 12
"""
def clockangle(hour,minute):
    angle = 0 # presenting the result
    if hour == 12:
        angle = minute * (.5) # so if minute is 0, then angle = 0
    elif hour < 12 and minute == 0: # if hour hand on the hour
        angle = hour * (30) # 30 degrees for every hour; 360 / 12
    else: # if minute != 0
        angle = hour * (30) + minute * (.5) # 0.5 degrees for every minute; 30 degrees for every hr/60 minutes
    return angle

print (clockangle(hour,minute))
"""
# Write a function that takes in an integer N and returns
# the sum: 1! + 2! + 3! + ... + N!

# userinput = int(input())
"""
x = 5
def factorialsum(x):
    resultlist = [] #this is where we'll add in factorials
    resultsum = 0
 #   n = 0 # use as incrementor
    for i in range(0,x): # we want loop to execute x-1 times
        n = 0
        resultproduct = 1 # reset to 1 for each digit of factorial
        if i == 0:
            x -= n
        else:
            x -= 1 # change x to create factorial for each x (e.g. 4,3,2,1..)
        while x > 1 and n < x: # let's say x = 3, n=0 - let's first do factorial of 3
            resultproduct *= x-n
            n += 1
        resultlist.append(resultproduct)
    for j in resultlist:
        resultsum += j
    return resultlist, resultsum
print (factorialsum(x))
"""

# understand why getting [6,1,1] if x = 3; can't understand [24,1,1,1] for x = 4 - 2nd digit should be 2
# try hardcoding outer while loop
"""
# Given a sequence of non-negative integers, where each number is written
# in a separate line. The sequence ends with 0.
# Determine the length of the widest fragment where all the elements are equal to each other.
"""
a = [1,7,7,7,7,7,9,9,9,9,1,0] # should be 7
count = 1
highestcount = 0
i = 0
while i < len(a)-1:
  if a[i] == a[i+1]:
      count += 1
      i += 1
      if count > highestcount:
          highestcount = count     
  else:
      i += 1
      count = 1
print (highestcount)
# this gives me 8; because it counts both dupe 7's & 9's
"""
# can use a dictionary; but you can't tell if they repeat..
a = [1,7,7,7,7,7,9,9,9,9,1,0,7]
dict1 = {}
endlist = [] # container for widest fragment
for i in range(0,len(a)-1): # for indexes of the list
    if a[i] == a[i+1] and a[i] in dict1:
        dict1[a[i]] += 1
    else:
        dict1[a[i]] = 1
print (dict1)
        
"""
