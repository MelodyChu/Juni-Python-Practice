"""
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

    """

def multiply2(numbers):
    largest = 0
    secondlargest = 0
    for c in numbers:
        if c > largest and c > secondlargest:
            secondlargest = largest
            largest = c
        if c < largest and c > secondlargest:
            secondlargest = c
    return largest * secondlargest
 
        

numbers = [10, 7, 9, 1]
print (multiply2(numbers))
"""
c,d
10,7 ignore
10,9 ignore
10,1 ignore
7,10 result = 10
7,9  result = 9
7,1
9,10
9,7
9,1
1,10
1,7
1,9
"""
"""
largestNumber
secondLargestNumber
[1,0,2,5,4]

going through the list:
    case 1: the number in teh list is greater than BOTH of the numbers
    case 2: the numebr in the list is only greater than ONE of the numbers
    case 3: the number in the list is not greater than either of the numbers """
