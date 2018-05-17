# merge sort; put together 2 lists a & b
# take first index from both lists; compare them ; see which one is bigger; sort
# assume both lists are sorted individually...? should be same length..?


x = [9,1,1,6,7,8,100]

def mergesort(x):
    if len(x) == 1:
        return x
    elif len(x) > 1:
        midpoint = int(len(x)/2)
        a = mergesort(x[0:midpoint])
        b = mergesort(x[midpoint:len(x)])
    return merge(a,b)
    

def merge(a,b):
    result = []
    while len(a) > 0 and len(b) > 0: #placeholder; while both lists lenght > 0
        # print ("top of loop")
        if a[0] > b[0]:
            result.append(b[0])
            b.remove(b[0]) # now b becomes [6,7,8]
            print (b)
        elif a[0] < b[0]:
            result.append(a[0])
            a.remove(a[0])
            print (a)
        else: # if both a[0] = b[0]
            result.append(a[0]) # pick a random conditional from above; doesn't matter which list it comes from
            a.remove(a[0])
            print (a)
        print (result)
    if len(b) == 0:
        result += a
    elif len(a) == 0:
        result += b
    return result
# print (merge(a,b))

print (mergesort(x))





"""
def mergesort(a,b):
    result = [] # new, end list
    for i in range(0,len(a)): # i is index; assume both lists are same length
        if a[i] > b[i]:
            result.append(b[i])
            # b.remove(b[i])
            result.append(a[i])
            # a.remove(a[i])
        elif a[i] < b[i]:
            result.append(a[i])
            # a.remove(a[i])
            result.append(b[i])
            # b.remove(b[i])
    return result
print (mergesort(a,b))

#i = 0, j = 0, a[0] = 4, b[0] = 1; result append b[0] then a[0]
# i = 1, j = 1; a[1] = 9, b[1] = 6; result append b[1] then a[1]
"""

"""Given two separate lists A and B ordered from least to greatest,
construct a list C by repeatedly comparing the least value of A to the
least value of B, removing the lesser value, and appending it onto C.
When one list is exhausted, append the remaining items in the other list
onto C in order. The list C is then also a sorted list."""

            
