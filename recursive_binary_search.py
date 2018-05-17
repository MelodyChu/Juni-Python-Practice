"""
a = [1,1,2,3,4,5,10]
x = 2
def binary(x,a):
    first = 0
    last = len(a)-1
    midpoint = int((first + last) / 2)
    # base case
    if len(a) == 0:
        return False
    elif a[midpoint] == x:
        return True
    elif x < a[midpoint]:
        return binary(x, a[0:midpoint])
    elif x > a[midpoint]:
        return binary(x,a[midpoint + 1:last+1])

print (binary(x,a))
"""
# rewrite of binary search iteratively
"""
a = [1,1,2,3,4,5,10]
x = 5
def binary(x,a):
    firstindex = 0
    lastindex = len(a)-1 #bc indexes start from 0
    while firstindex <= lastindex: #run loop until x is found; use while loop bc we don't know when we'll find x
        midpointindex = int((firstindex + lastindex)/2) # needs to reset every time
        if a[midpointindex] == x:
            return True
        elif x < a[midpointindex]:
            firstindex = 0
            lastindex = midpointindex - 1 # establish ranges
        elif x > a[midpointindex]:
            firstindex = midpointindex + 1
            lastindex = len(a)-1
    return False
print (binary(x,a))
"""

# bubble sort re-write #2
# we want outer loop to execute n-1 times to make sure everthing within is sorted
# we want inner loop to compare adjacent numbers to see which one is bigger and order accordingly. do a SWAP
"""
a = [4,1,3,1,7,10,2]
def bubble(a):
    #num = a[0]
    interim = a[0] # placeholder container variable
    for i in range(0,len(a)-1): #len(a)-1 because we're looking at pairs?
        for j in range(0,len(a)-1): # iterate through indexes of j
            if a[j] > a[j+1]: # if left numer greater than right number
                interim = a[j]
                a[j] = a[j+1] # make left number = right number
                a[j+1] = interim # make right number = left number
    return a
print (bubble(a))
"""
# first time through
# i = 0; j = 0; a[j] = 4 and a[j+1]=1; goes to first if statement; interim = 4; a[j] becomes 1; a[j+1] becomes 4
# [1,4,3,1,7,10,2]
# i = 1; j=1; a[j] = 4; a[j+1]= 3; goes to first if statement; a[j] becomes 3 and a[j+1] becomes 4
# [1,3,4,1,7,10,2] --> [1,3,1,4,7,10,2] --> [1,3,1,4,

#linear sort re-write #2
# we want the outer loop to execute n-1 times to find us the minimum each time
# we want inner loop to execute finding the minimum and placing the new minimums into a new list
"""
a = [4,1,3,1,7,10,2]
def linear(a):
    result = [] # container for the new list of sorted minimums
    for i in range(0,len(a)): # number of times to execute what's going on inside inner loop
        min1 = a[0] # minimum placeholder; why does it need to be here? What needs to be updated e/ time...
        for j in range(0,len(a)): # need to iterate through each index/number in list to put into mins
            if a[j] < min1:
                min1 = a[j]
        a.remove(min1) # take min out of list
        print (a)
        result.append(min1) # put min in new list
        print (result)
    return result
print (linear(a))
"""
# first time through
# i = 0, j = 0-6; min1 = 1; result = [1]
# 2nd time; i = 1, j=0-5; result = [1,1]
# 3rd time; i = 2, j=0-4; result= [1,1,2]
# NOTE: getting error line 75 -  list.remove(x): x not in list; execute first 2 loops
# ***Why can't min1 be outside of first for loop? why isn't it len(a) - 1***
    

# insertion sort re-write #1
# we are not creating a new list; instead we're building a sublist within the OG list
# we want outer loop to execute n-1 times to properly sort the next number within sublist
# compare first number outside sublist with all numbers within sublist; once finds number smaller, then put it nex to
"""
a = [4,1,3,1,7,10,2]
def insertion(a):
    interim = a[0] # interim; swap happens 
    for i in range(1,len(a)): # come back to the len part; # of times we want outerloop
        position = i # set position as index
        while a[position] < a[position-1]:
            interim = a[position]
            a[position] = a[position-1]
            a[position-1] = interim
            position -= 1
    return a
print (insertion(a))
"""
# 1st time through; i = 1; position = 1; a[1] < a[0] so swap [1,4,3,1,7]
# 2nd time through: i = 2; position = 2; a[2] < a[0] so swap [1,3,4,1,7

# what do we want
# 1: [4,1,3,1,7,10,2] sublist is 4
# 2: [1,4,3,1,7,10,2] sublist is 1,4
# 3" [1,3,4,1,7,10,2] sublist is 1,3,4
#4:  [1,1,3,4,7,10,2]
#5" [1,1,3,4,7,10, 2]

# struggles - getting while loop; setting position as i; iterating down the position unit

# selection sort attempt
# we want to loop through n-1 times (outer loop)
# inside loop; we want to keep appending the minimum to the front onto the growing sublist
a = [1,4,3,1,7]
def selection(a):
    for i in range(0,len(a)): # i is 0; if i is 1
        # position = i
        # print (position)
        # min1 = a[0] # placeholder for the min
        minindex = i
        # swapnum = a[0] # intermediary placeholder bc we will be swapping
        for j in range(i,len(a)): #if start finding minimums for rest of list
            if a[j] < a[minindex]: # standard find min
                # a[minindex] = a[j] #now need to swap values
                minindex = j
        print (a[minindex]) # this keeps printing 1
        swapnum = a[i] #save value of original
        a[i] = a[minindex] #set a[position] as minimum'
        a[minindex] = swapnum
  # k want j should be the minimum # inde <-- no j always goes to the end of loop
        print (minindex)
        print (a)
    return a
print (selection(a))

#1st time; i =0; position = 0; j = 0-7; min1 = 1; swapnum = 4; a[0] becomes 1; a[j] = 4
# [1,4,3,1,7]
#2nd time: i = 1; position = 1; j = 1-7; min1 = 1; swapnum = 4; a[1] becomes 1; a[j] = 4
# [1,1,3,4,7]
# issues: setting up while loop; doing swap wiht minimum (can't find index of orig # min has to switch with); minimum is same e/ time)
                
            



# assume first number is minimum
# we do minimum of the rest of list; see 1 is smallest; put 1 in the front (swap 1 & 4)
# start finding min of rest of the list; see that there is another 1. put that after 1st one



