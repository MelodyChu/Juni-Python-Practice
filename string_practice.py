"""s = input()
firsthalf = s[len(s)/2]
print (firshalf)"""
"""

# Given a string that may contain a letter f. Print the index of the first and last occurrence of f. If the letter f occurs only once, then output its index once. If the letter f does not occur, print -1.
s = input()
print (s.find('f'))
print (s.rfind('f'))
"""
"""
6.7 - halp!!
result = 0
while True:
  a = int(input())
  if a > result:
    result += a
  elif a == 0:
    break
print (result)
"""
# 6.8

"""
d = 0
result = 0
while True:
    a = int(input())
    if a > 0:
        d += 1
        result += a
    elif a == 0:
        break
print (result / d)
"""
#6.9 - not sure
"""
result = 0
while True:
    a = int(input())
    if a > result:
        result = a
    elif a == 0:
        break
p
"""
#6.A
"""
result = 0
while True:
    a = int(input()) # getting this err:R alueError: invalid literal for int() with base 10: ''
    if a % 2 == 0: 
        result += 1
    elif a == 0:
        break
print (result)
"""
#6.B - check
"""
result = 0
d = 0
while True:
    a=int(input())
    if a > result:
        result = a
        d += 1
    elif a == 0:
        break
print (d-1)
"""
# Fibonacci struggles - finish this

result1 = 0
result2 = 1
n = 1
d = 2
while d < n: #to test out
    result3 = result1 + result2
    result1 = result2
    result2 = result3
    d += 1
print (result3)

"""
"""
"""
s = [5,6,7,8,9]
a = [int(s) for s in input().split() if s % 2 == 0]
"""
# 7.2
"""
lst = [1,2,2,3,3,3,4]
for i in lst:
    if i % 2 == 0:
        print (i)
"""

#7.1 - for loop retry - how to do this in list comprehension?
"""
lst = [5,6,7,8,9]
for i in range(0,len(lst)+1):
    if i % 2 == 0:
        print (lst[i])
"""

#7.3
"""

lst = [1,5,2,4,3]
result = []
for i in range(1,len(lst)):
    if lst[i] > lst[i-1]: 
        result.append(lst[i])
print (result)
"""

#7.4 - -
"""

lst = [-1,1,-2,3,-1, 2]
result = []
for i in range(1,len(lst)+1):
    if (lst[i] > 0 and lst[i-1] > 0) or (lst[i] < 0 and lst[i-1] < 0):
        print (lst[i], lst[i-1])
        break
else: # where should i put else to stop this from printing automatically?
    print ('0')
"""
#7.5
"""
lst = [1,2,2,3,3,3]
result =0
for i in range(0,len(lst)):
    if lst[i] != lst[i-1]:
        result += 1
print (result)
"""
#7.6 -- swaps?
"""
lst = [1,2,3,4,5]
result = []
for i in range(0,len(lst)):
    if i % 2 != 0: #for all odd indices
        lst[i] = lst[i-1]
"""
 #8.1 -- not sure about nested loops; below prints into 1 vertical line

a = [[11,12,13,14],[21,22,23,24],[31,32,33,34]]
c = 2
for m in a: # m is rows
  for n in m: # n is elements
      n = n*c
print (a)
    


    
    
    
