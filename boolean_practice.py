# write a function that takes in a list of lists.
# return True if the number 1 is contained inside all of the sublists
# else return False
# ex. [[0,1],[1,2,3],[1,3]] -> return True

x = [[0,1],[1,2,3],[1,3]] 
y = [[1,0],[0,0],[1,0]]
z = [[1,1],[1,9],[1,2,3,4,5]]

def check(x):
    for sublist in x: # looking at individual sub lists
        if 1 not in sublist:
            return False
    return True
print (check(x))
print (check(y))
print (check(z))

# rewrite answer as script instead of function

# write a function that takes in a list of lists AND a nunber n
# return True if the number n is contained inside all of the sublists
# do the first 3 of interviewcake
