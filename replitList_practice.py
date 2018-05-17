# 7.7 Swapping lists
"""
a = [1,2,3,4,5]
d = 1 # set to something in list
for i in range(1,len(a)):
  if i % 2 != 0: # if index of number in list is odd
        d = a[i-1] # d holds value of 2; d= a[1]
        a[i-1] = a[i]
        a[i] = d
print (a)
"""
# 7.8 - swap max & min
"""
a = [3,4,5,2,1]
result = []
maxindex = 0
maxval = 3
minindex = 0
minval = 3
for i in range(0,len(a)): # find index of number in a
    if a[i] > maxindex:
        maxindex = i # find index of max
        maxval = a[i] # find value of max
    elif a[i] <= minindex: # can't figure out how to do min without having it set to 0
        minindex = i
        minval = a[i]
print (maxindex, minindex)
"""
#7.9 - count number of pairs of equal elements (see repl.it)
"""
a = [1,2,3,2,3]
result = 0
for i in range(0,len(a)): # iterate through indexes of a
    for j in range(i,len(a)): # iterate through indexes of a
        if a[i] == a[j] and i != j: # if digits are same and indexes are NOT same
            result += 1
print (result)
"""
# try 7.9 with dictionaries
a = [1,2,3,2,3]
dict1 = {}
result = 0
for i in a:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
print (dict1)
for i in dict1:
    if dict1[i] == 2:
        result += 1
print (result)
        

#7.B - review dictionaries; can also do sets apparently
"""
a = [4,3,5,2,5,1,3,5]
dict1 = {}
result = []
for key in a:
    if key in dict1:
        dict1[key] += 1
    else:
        dict1[key] = 1
print (dict1)
for key in dict1:
    if dict1[key] == 1:
        result.append(key)
print (result)
        
"""

# 7.9 redo -- more elegant way to do this?
"""
a = [-1,-2,-3]
result = []
maxindex = 0
maxval = a[0]
minindex = 0
minval = a[0]
for i in range(0,len(a)): # find index of number in a
    if a[i] > maxval:
        maxindex = i # find index of max
        maxval = a[i] # find value of max
    elif a[i] < minval: # can't figure out how to do min without having it set to 0
        minindex = i
        minval = a[i]
print (maxindex, minindex)
for j in range(0,len(a)):
    if j == maxindex: # if j = 2
        a[j] = a[minindex] #  replace a[2] with a[4]
    elif j == minindex: # if j = 4
        a[j] = maxval
print (a)
    """

            
    
