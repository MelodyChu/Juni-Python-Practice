"""def multiply(numbers):
  max1 = 0 
  result = 0 
  for i in numbers:
    if i > result:
      i = result
  return i

numbers = [1,7,10,11,10]
print (multiply(numbers))
"""

def multiply(numbers):
    result = 0
    for i in numbers:
        for j in numbers:
            if i > j:
                result = i
    return result

numbers = [1,7,10,110,10]
print (multiply(numbers))



