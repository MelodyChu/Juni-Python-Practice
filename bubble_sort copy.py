"""a = [4,3,5,1,2]
def bubble(a):
    interim = 0 # temp variable needs to be in the beginning
    for i in range(0,len(a)):
        for j in range(0,len(a)-1):
            if a[j+1] < a[j]:
                interim = a[j+1] #save interim into something useful!
                a[j+1] = a[j]
                a[j] = interim
    return a
print (bubble(a))
"""
#linear sort - rewrite
a = [4,3,5,1,2]
def linsort(a):
    endlist = [] # append minimums here
    for i in range(0,len(a)): # outer loop; need to execute loop len(a) times
        result = a[0] #placeholder
        for j in range(0, len(a)):
            if a[j] < result:
                result = a[j]
        print (result)
        print (a)
        a.remove(result)
        endlist.append(result)
    return endlist
print (linsort(a))

"""
# online example of implementation:http://danishmujeeb.com/blog/2014/01/basic-sorting-algorithms-implemented-in-python/
def bubble_sort(items):
        """ Implementation of bubble sort """
        for i in range(len(items)):
                for j in range(len(items)-1-i):
                        if items[j] &gt; items[j+1]:
                                items[j], items[j+1] = items[j+1], items[j]     # Swap!
        
