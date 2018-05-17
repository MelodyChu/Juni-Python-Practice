# write a function that takes in a list of lists AND a nunber n
# return True if the number n is contained inside all of the sublists
"""
list1 = [[1,2,3],[3,5,1],[1,7,6],[1,1,1],[2,2,2]] # example
n = int(input())
def findn(list1):
    for i in list1: #iterating through each list within list1
        if n not in i: #if the integer n is not in the sub-list
            return False
            print ('false')
    else:
        return True
        print ('true')
print (findn(list1))
"""
# write as script -- why is this so different than a function?

list1 = [[1,2,3],[3,5,1],[1,7,6],[1,1,1],[1,2,2]] # example
n = int(input())
countofi = 0
for i in list1:
    if n not in i: #if the integer n is not in the sub-list
        print ('false')
        countofi += 1
if countofi == 0:
    print ('true')
"""
# attempt at using booleans -- still getting dupes

list1 = [[1,2,3],[3,5,1],[1,7,6],[1,1,1],[1,2,2],[0,0,0]] # example
n = int(input())
inlist = False #can this be false or true? is this where the boolean needs to be placed?
for i in list1:
    if n not in i: #if the integer n is not in the sub-list
        inlist = False # previously, i said list1=true
        print ('false')
if inlist != False:
    print ('true')
"""
