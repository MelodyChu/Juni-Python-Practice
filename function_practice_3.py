for i in range(1,51):
  if i % 3 == 0 and i % 5 == 0: # checking to see if # is multiple of 3 & 5
    print ("Fizzbuzz")
  elif i % 5 == 0:
    print ("Buzz")
  elif i % 3 == 0:
    print ("Fizz")
  else:
    print (i)



# thought process:
# outcome: for [1,2,5,6,7,10] return 7*10
# approach 1: do a sort to find the highest 2 numbers at end of array
# approach 2: find the highest sum of 2 numbers; try this
# loop to find highest number; then loop to find the 2nd highest number; thought about doing another nested loop or even creating a 3rd variable
# remove the highest number from the array; execute loop again to find next highest

# approach 2

def multiply(numbers):
    result = 0
    product = 0
    for a in numbers:
       for b in numbers:
            if a + b > result and a != b: # sum of largest 2 numbers should also be largest sum
                result = a + b
                product = a * b
    return variable # why do i have to create a new variable, and can't return a*b?
    
"""
numbers = [1,3,1,4,9,10,21]
print (multiply(numbers))

# initial approach (stuck)

"""

def multiply(numbers): # figure out highest number
    result = 0
    for c in numbers:
        for d in numbers:
            if d > c and d != c: # d > c, and c > all other numbers; thought about somehow holding d constant and subtracting c to get the lowest difference
                result = d

"""

def multiply(numbers):
    numbers.sort(key = int)
    for a in range((len(numbers)-1, len(numbers)+1):
        return a

numbers = [1,3,1,4,9,10,21]
print (multiply(numbers))
