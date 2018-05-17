"""a = [4,3,5,1,2]
def linsort(a):
    newlist = []
    while len(a) > 0:
        result = a[0]
        for i in a:
            if i < result:
                result = i
        print(a)
        print(result)
        a.remove(result)
        newlist.append(result)
    return newlist
print (linsort(a))
"""

a = [4,5,3,8,2]
def bubble(a):
    interim = 0
    for i in range(0,len(a)):
        for j in range(0,len(a)-1):
            if a[j+1] < a[j]:
                interim = a[j+1] #set interim = to this
                a[j+1] = a[j]
                a[j] = interim
    return a
print (bubble(a))
