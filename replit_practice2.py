"""a = int(input()) # 1234
b = a % 10 # =4
c = ((a - b)/10) % 10 # 1230/10 = 123; 123/10 % = 3
print (c*10 + b) """

"""# Find tens digit
a = int(input())
b = a % 10 #single digit
c = ((a - b)/10) % 10 #1230
print (c) """

"""
# Given 3 digit number find sum of digits
a = int(input()) # 123
b = a % 10 # single digit # 3 
c = ((a - b)/10) % 10 # tens digit #2
d = (a - c*10 - b)/100 # 123 - 20 - 3 / 100
print (b + c + d) """

"""
# given float, print number to right of decimal
a = float(input()) #1.79
b = 10 * a #17.9
c = int(b) % 10
print (c)
"""
"""
# create function such that kilometers / route length = number of days
n = int(input()) #4
m = int(input()) # 8
print (int(m/n) + 1)
700
"""

"""
a = int(input()) #20
b = int(input()) #21
c = int(input()) #22

num_desksa = int(a / 2) + (a % 2)
num_desksb = int(b / 2) + (b % 2)
num_desksc = int(c / 2) + (c % 2)

print (num_desksa + num_desksb + num_desksc)
"""

# Given three integers. Determine how many of them are equal to each other. The program must print one of the numbers: 3 (if all are same), 2 (if two of them are equal to each other and the third one is different) or 0 (if all numbers are different).

"""
a = int(input())
b = int(input())
c = int(input())

if a == b and a == c:
    print ('3')
elif a == b or a == c:
    print ('2')
else:
    print ('0')
"""

"""

# chessboard question: can only move horizontally & vertically; needs to be able to do it in one step
xaxis = int(input()) # 1-8
yaxis = int(input()) # 1-8
newx = int(input())
newy = int(input())

if xaxis == newx and abs(newy - yaxis) == 1:
    print ("YES")
elif yaxis == newy and abs(newx - xaxis) == 1: #if y coordinate says same moves horizontally
    print ("YES")
elif xaxis == newx and yaxis == newy: # if chess piece doesn't move
    print ("YES")
else:
    print ("NO")
"""
"""
a = int(input())
b = int(input())
for i in range(a,b+1):
  print (i)
"""
"""
N = int(input())
result = 0
for i in range(1,N+1):
  result += i ** 3
print (result)
"""
"""
a = int(input())
result = 1
for i in range(1,a+1):
  result *= i
print (result)
"""
"""
to revisit:

alist = [5,0,700,0,200,2]
result = 0
for i in alist:
  for j in alist:
      if i + j == 0:
        result += 1
print (result)
"""
"""
a = int(input()) # 3
result = 0
factorial = 1
for i in range(1,a+1):
  factorial *= i # store the factorial before it
  result += factorial # we want 1 + (2*1) + (3*2*1)
print (result)
"""
"""
# why is it printing 64 when I input 50?
N = int(input())
i = 0
while i ** 2 < N:
    i += 1
    print (i ** 2)
"""
"""
a = int(input()) # not less than 2
i = 2
while i > 1:
    i += 1
    if a % i == 0:
        print (i)
        break
"""
"""
x = int(input())
n = 0
while 2 ** n <= x:
  n += 1
print (n, 2 ** n)
"""
"""
# need to check this
miles1 = int(input())
miles2 = int(input())
totalmiles = miles1
d = 0
while totalmiles <= miles2:
    totalmiles *= 1.1 
    d += 1
print (d)
"""
"""
# 6.5: for loop here gives me 4;
a = [1,7,9,0,5]
result = 0
for i in a:
    if i != 0:
        result += 1
print (result)

# while loop
"""
"""
a = [1,7,9,0,5]
result = 0
i =
while i != 0 in a: # while i not equal in 0 in the list..
  result += 1
print (result)
"""
"""
x = int(input())
n = 0
while 2 ** n <= x:
  n += 1
print (n-1, 2 ** (n-1))

# or
n = 0
while True:
    if 2** <= x:
        n+=1
    else:
        break

"""
"""
miles1 = int(input())
miles2 = int(input())
totalmiles = miles1
d = 0
while totalmiles <= miles2:
    totalmiles *= 1.1 
    d += 1
print (d)
"""
result = 0
while True:
  a = int(input())
  if a > result:
    result = a
  elif a == 0:
    break 
print (result)
