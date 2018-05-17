# Create and print a dictionary where the keys are the numbers 1-100 and the values are the square of that number
# Write a function that takes in a word and returns a dictionary, where the keys are the letters in teh word and the values are teh number of times they appear in the word

# Hint: look up the Python 'in' dictionary operator

"""

animals = {"panda": "big", "algae": "small"}

numbers = {"one": 5, "two": 3}

numbers["one"] += 1

print(numbers)

"""
"""
key = int()
value = int()
dictionary = {key:value}
for i in range(1,101):
    dictionary.key = i
    dictionary.value = i ** 2
    
print(dictionary)
"""
"""
squares = {x: x**2 for x in range(1,101)}
print (squares)
"""

def squares2():
    dictionary = {}
    for x in range(1,101):
        dictionary[x] = x ** 2
    return dictionary


print (squares2())

"""

def makedict(word):
    new_dict = {}
    for i in word:
        if i not in new_dict:
            new_dict[i] = 1 #for new_dict, set i as key and 1 as value
        else:
            new_dict[i] += 1
    return new_dict
        

word = 'ibis'
print (makedict(word))

"""
"""
        for j in word:
            if i == j:
                count += 1
                result.append(count)
            else:
                result.append(count)
    return result
"""
       

"""
seq = ('number', 'square')
dict = dict.fromkeys(seq)
"""


"""
class dictionary(object):
    def __init__(self, number, square):
        self.number = number
        self.square = square
for i in object:
"""
"""
for j in word:
            if i == j:
             new_dict[i] += 1
            
        new_dict.keys = i
     else:
         new_dict.values += 1
 return new_dict
 """
