# Sum of range in sequence
"""
n = 2

def series_sum(n):
    result = 1.00
    startingnum = 1
    if n == 1:
        result = 1.00
    for i in range(2,n+1):
        startingnum += 3.00
        result += 1 / (startingnum)
    return str("{0:.2f}".format(result))
print (series_sum(n))
"""
#Facebook like button question
"""
#names = ['Alex', 'Jacob', 'Mark', 'Angela']

names = []

def likes(names):
    #your code here
    if len(names) == 0:
        print ("no one likes this")
    elif len(names) == 1:
        print (names[0] +  "likes this")
    elif len(names) == 2:
        print (names[0] + " and " + names[1] + " like this ")
    elif len(names) == 3:
        print (names[0] + " , "+ names[1] + " and " + names[2] + " like this")
    elif len(names) >= 4:
        print (names[0] +" , " + names[1] + " and " + str(len(names) - 2) + " others like this ")
    return 
print (likes(names))
"""
# sum of smallest numbers
"""
numbers = [19, 5, 42, 2, 77]
def sum_two_smallest_numbers(numbers):
    result = [] # house the 2 smallest numbers
    for i in range(0,2): # we want outer loop to execute twice
        min1 = numbers[0] # placeholder variable to find minimum
        for j in range(0,len(numbers)): # need to iterate through all numbers
            if numbers[j] < min1:
                min1 = numbers[j]
        numbers.remove(min1)
        result.append(min1)
        print (result) #check
    return result[0] + result[1]
print (sum_two_smallest_numbers(numbers))
# initially, i = 0; j = 0-4; min1 = 2; numbers [19,5,42,77] result = [2]
"""
# reverse individual words in a sentence
"""
str = "This is an example!"
def reverse_words(str):
    result = ""
    stringlist = str.split() # transform to list
    for i in stringlist:
        result += " " + i[::-1] + " "
    return result
print (reverse_words(str))
  #go for it
  """
# find the one unique number in the list
"""
arr = [0, 1, 1, 1, 1, 1]
def find_uniq(arr):
    if arr[0] != arr[1]: #see if we can find in firs pass
        if arr[0] == arr[2]:
            return arr[1]
        elif arr[1] == arr[2]:
            return arr[0]
    for number in range(2,len(arr)):
        if arr[number] != arr[number-1]:
            return arr[number]
print (find_uniq(arr))
"""
# find sum
"""
begin_number = 0
end_number = 15
step = 3
def sequence_sum(begin_number, end_number, step):
    result = 0 # to hold result sum; result = 1
    if begin_number > end_number:
        result = 0
    else:
        for number in range(begin_number,end_number+1,step): #2,4,6
            print ("check")
            print (number)
            result += number
            print (result)
    return result
print (sequence_sum(begin_number, end_number, step))
# 1st time: increment = 3; result + increment = 4
    """
