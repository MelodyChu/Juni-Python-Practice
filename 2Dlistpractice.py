#8.1 -- not sure about nested loops; below prints into 1 vertical line
"""
a = [[11,12,13,14],[21,22,23,24],[31,32,33,34]]
c = 2
for m in range(len(a)): # m is rows
  for n in range(0,len(a[m]): # n is elements
      a[m][n] = a[m][n] * c
print (a)
    
"""

#8.2 -- find maximum
"""
a = [[0,3,2,4],[2,3,5,5],[5,1,2,3]]
result = 0
for m in range(len(a)): # find number of rows (index)
  for n in range(0,len(a[m])): # find the number of elements (index):
    if a[m][n] > a[m-1][n-1]:
      result = a[m][n]
print (result,m,n) # not sure why this doesn't work; prints correct result
"""
#8.4 -- come back to this

n = 5
a = [[0] * n for i in range(n)] # do we always need to set this up first?
d = 1 # increment up
for i in range(n):
    for j in range(n):
        a[i][j]=abs(i-j)
for row in a:
    print(' '.join([str(elem) for elem in row])) # what is this supposed to do

# i = 0, j = 1; d = 1
# i = 1, j = 0; d = 1
# i = 1, j = 2; d= 1
# i = 2, j = 1; d= 1
# i = 2, j = 3; d=1
#i = 3, j = 2; d= 1
#i = 3, j = 4; d= 1
# i = 4; j = 3; d= 1


a = [1,2,3,2,1]
len(set(a))
"""
# if i == j: # diagonal = 0
            a[i][j] = 0
        elif i > j and i - j == d: # if i = 2 and j = 1; want d to = 1; if i= 3 and j=4; d = 1
            a[i][j] = d
            d += 1
        elif j > i and j - i == d:
            a[i][j] = d
            d += 1
"""
# 8.5 - antidiagonals

n = 6
a = [[0] * n for i in range(n)] # do we always need to set this up first?
for i in range(n):
    for j in range(n):
        if i + j == n-1:
          a[i][j] = 1
        elif i + j < n-1:
          a[i][j] = 0
        elif i + j > n-1:
          a[i][j] = 2
for row in a:
    print(' '.join([str(elem) for elem in row])) 

