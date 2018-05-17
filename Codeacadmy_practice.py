#Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.

# For example: anti_vowel("Hey You!") should return "Hy Y!". Don't count Y as a vowel. Make sure to remove lowercase and uppercase vowels.
"""
n = str(input())
def anti_vowel(n):
    output = ''
    for i in n: #iterate through the string - 
        if i not in "aeiouAEIOU": # - why does 'if i != 'a' or i != 'o' etc. not work?)
            print (i)
    return 
print (anti_vowel(n))
"""

# To the right is a dictionary containing all of the letters in the alphabet with their corresponding Scrabble point values.

# For example: the word "Helix" would score 15 points due to the sum of the letters: 4 + 1 + 1 + 1 + 8.
"""
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

word = str.lower(input())

def scrabble_score(word):
    total = 0
    for i in word: # iterate through letters of the word
        total += score[i]
    return total

print (scrabble_score(word))
"""
# Write a function called censor that takes two strings, text and word, as input.
# It should return the text with the word you chose replaced with asterisks.
"""
text = 'this hack is wack hack'
word = 'hack'
def censor(text,word):
    splitwords = text.split(' ') #break apart text into individual words
    result = '' #container for resulting string
    for i in splitwords: # iterating through words instead of letters
        if i == word:
            i = len(word) * '*' #replace word with astricks -- why doesn't this work?
        result =' '.join(splitwords)
    return result
print (censor(text,word))
"""
"""
#first try
 #   result = '' #printing the end phrase with censors
    if word in text: #we want to find the whole word, not iterate each letter
 #       word = '*' * len(word) #use astericks to correspond to letters of word
        text.replace(word,(len(word))*('*'))
    return text
print (censor(text,word))
"""
# Codeacademy answer: - come back to this
"""
def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result
"""
# Define a function called count that has two arguments called sequence and item.

# Return the number of times the item occurs in the list.

# For example: count([1, 2, 1, 1], 1) should return 3 (because 1 appears 3 times in the list).
"""
sequence = [1, 2, 1, 1,1,1,1]
item = 1
def count(sequence, item):
    result = 0 # container for the answer
    for i in sequence: # iterate through e/ number in list
        if i == item:
            result += 1
    return result
print (count(sequence,item))
"""
# Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, and returns the result. For example, purify([1,2,3]) should return [2].

# Do not directly modify the list you are given as input; instead, return a new list with only the even numbers.
"""
list1 = [1,2,3,4,5,1,2]
def purify(list1):
    result = [] #container for answer
    for i in list1:
        if i % 2 == 0:
            result.append(i)
    return result
print (purify(list1))
"""

# Write a function remove_duplicates that takes in a list and removes elements of the list that are the same.

# For example: remove_duplicates([1, 1, 2, 2]) should return [1, 2]. -- practice with dictionary
"""
list1 = [1, 1, 2, 2,3,1,1,5]
def remove_duplicates(list1):
    result = []
    for i in list1: #iterate through integers in list1
        if i not in result:
            result.append(i)
    return result
print (remove_duplicates(list1))

"""

# retry above with dictionaries:
"""
list1 = [1, 1, 2, 2,3,1,1,5]
def remove_duplicates(list1):
    resultdict = {}
    resultlist = []
    for i in list1: #iterate through integers in list1
        if i in resultdict: #remember to check if number is in dictionary first!
            resultdict[i] += 1
        else:
            resultdict[i] = 1
    for key in resultdict:
        resultlist.append(key)
    return resultlist
print (remove_duplicates(list1))
"""

# Write a function called median that takes a list as an input and returns the median value of the list. For example: median([1, 1, 2]) should return 1.
"""
list1 = [7,3,1,4]


def median(list1):
    sortlist = sorted(list1)
    result = 0
    i = len(sortlist)/2 # i is median index within sortedlist
    if len(sortlist) % 2 != 0: # length of list is odd
        result = sortlist[int(i)] #round number up i to get index
    else: # if length list is even
        result = (sortlist[int(i-1)] + sortlist[int(i)])/2
    return result
print (median(list1))
"""

#Replit String practice
# print index of 2nd p
# if no p, print -2; if 1 p, print -1
"""
s = input()
countofp = 0
foundfirstp = False
for i in s: #iterate through the index of each letter
  if i in 'pP':
    countofp += 1
print (countofp)
if countofp == 0:
    print ('-2')
elif countofp == 1:
    print ('-1')
else:
    for i in range(0, len(s)): #let's use 'poop'
      if s[i] in 'pP':
          if foundfirstp == True:
              print(i)
              break
          else:
              foundfirstp = True
      
print (countofp)
#
for i in range(0, len(s)):
  if countofp == 1:
    print ('-1')
  elif countofp >= 2:
    print (i)
"""
"""
# Replit dictionaries
list1 = ['apple','orange','banana','banana','orange','orange','orange']
dict1 = {}
maxnum = 0
for fruit in list1:
  if fruit in dict1:
    dict1[fruit] += 1
  else:
    dict1[fruit] = 1
print (dict1)
for fruit in dict1:
  if dict1[fruit] > maxnum:
    maxnum = dict1[fruit]
print (fruit) #figure out how to print corresponding fruit to maxnum
"""
# come back to this - prior hackbright question
"""
list1 = [-1,5,-1,2,5,-1,-5]
def sumzero(list1):
    iszero = False
    for i in range(0,len(list1)):
        for j in range(0,len(list1)):
            if list1[i] + list1[j] == 0 and i != j:
                iszero = True
        # else:
            # iszero = False
    return iszero
print (sumzero(list1))
"""
# Implement count_substr(input_str,substr) returns the number of times the sub_str occurs in string
"""
input_str = 'joemelojoejoejoe'
substr = 'joe'
def count_substr(input_str,substr):
    result = 0
    for i in range(0,len(input_str)):
        if input_str[i:i+len(substr)] == substr:
            result += 1
    return result
print (count_substr(input_str,substr))
"""
# Write a function that returns the cumulative sum of elements in a list

# assert solution([1,1,1]) == [1,2,3]
# assert solution([1,-1,3]) == [1,0,3]
"""
list1 = [1,-1,3] # as example
def solution(list1):
    result = [] # result is an output list
    sums = list1[0]
    for i in range(0,len(list1)): # iterate through each number in i
        if i == 0: # if i is in 0 index:
            result.append(list1[i])
        else: # if i is greater than 0
            sums += list1[i]
            result.append(sums)
    return result


print (solution(list1))
"""
# Write a function that, when given a list of words, returns a list of the words excluding any and all words that start with “d”, any and all words starting with “S” (capitalized), and any and all words whose lengths are longer than 4.

#For example, if the input list were the following:
#[“home”, “cat”, “Soup”, “coffee”]

#The function should output the following:
#[“home”, “cat”]

inputlist = ['home','cat','Soup','coffee','snak']
def words(inputlist):
    result = []
    for i in inputlist: #iterating through every word
        if len(i) <= 4 and i[0] not in 'dS': #length cannot exceed 4 and first letter cannot be d or S
            result.append(i)
    return result

print (words(inputlist))
        




