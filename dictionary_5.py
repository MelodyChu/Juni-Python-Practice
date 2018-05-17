def frequency(numbers):
    result = {} #use a dictionary
    final = []
    for i in numbers: # think about how to store it as a data type; does it need a variable?
        if i not in result:
            result[i] = 1
        else:
            result[i] += 1 # now for every number, we have counts of each number
            # {1:1, 2:3, 3:3, 4:3}
    max_val = 0
    for j in result:
        if result[j] > max_val:
            max_val = result[j]
            final = []
            final.append(j)
        elif result[j] == max_val:
            final.append(j)
    #for res in result:
  #      if result[res] == max_val:
 #           final.append(res)
    return final
    
numbers = [1,2,2,2,3,3,3,4,4,4]
print (frequency(numbers))
