# Dictionaries A.4 -- does dictionary always print the alphabetical lower key?
"""
fruits = ['apple', 'orange', 'banana', 'banana', 'orange']
dict1 = {}
result = 0
for fruit in fruits:
  if fruit in dict1:
    dict1[fruit] += 1
  else:
    dict1[fruit] = 1
print (dict1)
for fruit in dict1:
  if dict1[fruit] > result:
    result = dict1[fruit] #find maximum
print (fruit)
"""
# Dictionaries A.5 -- check this
"""

dict1 = {'helloworld.exe':['R','X'],'pinglog':['W','R'], 'nya':['R'], 'goodluck':['X','W','R']}
for key in dict1:
    userfile = input("Choose a file ")
    userinput = input("What command would you like to use? Choose R,X,or W! ")
    if userinput in dict1[userfile]:
        print ('ok')
    else:
        print ('access denied')
"""
# A.6 -- why does this loop only execute twice?

dict1 = {'USA':['Boston', 'Pittsburgh', 'Washington','Seattle'], 'UK':['London', 'Edinburgh','Cardiff','Belfast']}
cityinput = input("Input a city ")
foundCountry = False
for country in dict1:
    if cityinput in dict1[country]:
        countryName = country
        foundCountry = True
if foundCountry  != True:
    print("not found")

        

# A.7 -- how do you sort dictionary by values and alphabetize?
"""text = ['hi','hi','what','is','your','name','my','name','is','bond','james','bond','my','name','is','damme','van','damme','claude','van','damme','jean','claude','van','damme']
dict1 = {}
for word in text:
    if word in dict1:
        dict1[word] += 1
    else:
        dict1[word] = 1
print (dict1)
"""
# A.1 -- check
"""
listnum = ['one','two','two','one','two','three','two','four','three', 'three', 'three']
result = []
dict1 = {}
a = 0
for number in listnum: # iterate through number strings
    if number not in dict1: #if number not in dict, put in dict and count 0
        dict1[number] = 0 # replace 0 for a for now
        result.append(0)
    elif number in dict1: # if number is in dict, count previous instance
        dict1[number] += 1 # i guess this works because you start the count at 0
        result.append(dict1[number])
print (dict1, result)
"""
