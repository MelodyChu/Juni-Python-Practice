#  try implementing selection sort going in the other direction
# (i.e. starting from the end of the list and continuously placing the
# largest number toward the right side of the list),
# once find the max in 1st iteration, do swap. max needs to go to end of list, and swapped number needs to go to index of original max

lista = [10,4,30,7,1,15,2]
def selection(lista):
    for i in range(0,len(lista)): # number of times outer loop need to execute
        # position = i #placeholder for keeping track of posiion
        max1 = lista[0] #max value placeholder 
        maxindex = 0 #max index placeholder
        for j in range(0, len(lista)-i): #start evaluation from 0 until end of list
            if lista[j] > max1:
                max1 = lista[j] # finding the max value of this iteration
                maxindex = j #make sure to assign maxindex to j to keep track of index of current max
        print (max1)
        print (maxindex)
        interim = lista[len(lista)-1-i] #save value of number that needs to be swapped with max
        print (interim)
        lista[len(lista)-1-i] = max1 # put maximum into end of list
        print (lista)
        lista[maxindex] = interim #put interim value into original index of max; i messed up here again and put J here at first! LOL
        print (lista)
    return lista
print (selection(lista))

# if i=0, max1 = 1; j = 0-4; max1 = 7; j = 3; interim = 1; max1 goes into last index of list; a[3] becomes 1
# lista = [1,4,3,1,7]
# i = 1, max1 = 1; j = 0-3; max1 = 4; maxindex = 1; interim = 1;max1 goes into 2nd to lsat index of list; a[1] becomes 1
        
# i goes from 0 to 4
# j goes from 0 to 4 (when i = 0), 0 to 3 (when i = 1), 0 to 2 (when i =2) , 0 to 1 (when i = 3) and 0 to 0 (when i = 4)
# lessons learned: j always iterates UNTIL THE END; length of list in index form needs adjustments (-1); you can create temp variables *when you need them* - doesn't always need to be defined in begnining
