# merge sort attempt
a = [1,1,2,3,4,5,10]
def mergesort(a,lefthalf,righthalf):# what should variable inputs be? would recursive here beo only for splitting list
    if len(a) == 1: #base case; if length of list is 1, return list (no need to sort)
        return a
    if len(a) > 1:
        midpoint = len(alist)/2
        lefthalf = alist[:midpoint]
        righthalf = alist[midpoint:]

        mergesort(lefthalf)
        mergesort(righthalf)




# rewrite of binary search iteratively -- reference
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
