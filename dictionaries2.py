# function that takes in a list of numbers and return a list of numbers that occurs most frequently
# [1,1,2,2,3,3,4] return [1,2,3]

def frequency(numbers):
    result = {} #use a dictionary
    variable = 0
    for i in numbers: # think about how to store it as a data type; does it need a variable?
        if i not in result:
            result[i] = 1
        else:
            result[i] += 1 # now for every number, we have counts of each number
    for x in result: # x is the key
        if result[x] > variable: #if the value of x is > than variable
            variable = result[x] #then the variable = the value, which becomes the new benchmark
    return result
 
        else:

def multiply(numbers): # figure out highest number
    result = 0
    new = 0
    for c in numbers:
        if c > result:
            result = c
    for d in numbers:
        if d > new and d != result:
            new = d
    print (new, result)
    return new * result

            
            
            
            
            
            
            
            
    return result


numbers = 
            
            
            
            




    # {1:2, 2:2, 3:2, 4:1}
    # need to use pairs of data; ID's are numbers and values are how many times they appear

    # How many letters does it take to spell out the numbers from one to ninety nine? Don't count any spaces or hyphens.
    # Hint: you'll need to use a dictionary.
