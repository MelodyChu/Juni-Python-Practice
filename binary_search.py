# #variable first, and variable last (len(list))
a = [1,1,2,3,4,5,10]
x = 2
def binary(x,a):
    first = 0
    last = len(a)-1
    # found = False # could we have done without defining boolean? 
    while first <= last: #and not found:
        midpoint = int(first + ((last-first)/2)) #or (first + last) / 2; what needs to be updated each time
        if a[midpoint] == x:
#            #found = True
            #print ("True")
            return True
        elif x < a[midpoint]: # x= 2
            last = midpoint - 1 #updating last
            print (last)
        else: 
            first = midpoint + 1 #updating first
            print (first)
    # print ("False")
    return False
    
print (binary(x,a))
"""
Initially:
midpoint = 4 (value = 5)
looking for x =7
so new sublist is midpoint 4 (value 5) to index 8 (value 8)
new midpoint is 6 (value 6)
go into while loop, 7 > 6
first = midpoint 6; last = 8
mid point = 7 ; value = 7
should return true
"""

# initial, incorrect solution
"""a = [1,2,3,4,5,6,6,7,8]
x = 1 
def binary(x,a):
    first = 0
    last = len(a)-1
    counter = 0
    midpoint = int(first + ((last-first)/2)) #or (first + last) / 2
    if a[midpoint] == x:
        return True
        print ("True")
    while a[midpoint] != x:
        if x < a[midpoint]: # x= 2
            last = midpoint - 1 #updating last
            print (last)
        elif x > a[midpoint]: 
            first = midpoint + 1 #updating first
            print (first)
    return False
    print ("False")
print (binary(x,a))"""

# reference: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html
