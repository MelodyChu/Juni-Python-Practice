#Selection sort - writing the algorithm

alist = [5,1,7,10,20,2]
def selection(alist):
    max1 = alist[0] # placeholder variable
    displaced = alist[0] # swapping number for max
    i = 1 # incrementor
    while i <= len(alist)-1: # for i in range(0,len(alist)-1): # number of time we want loop to execute
        for number in range(0,len(alist)):
            if alist[number] > max1:
                max1 = alist[number]
        displaced = alist[len(alist)-i] #save number at end value in displaced
        alist[len(alist)-i] = max1 #then make the number at the end become max1(largest number)
# need to figure out ohw to make index of max1 (in previous position) = to displaced
        i += 1
        
        for alist
