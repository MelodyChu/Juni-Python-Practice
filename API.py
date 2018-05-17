import requests # compared to urllib
import json
#import urllib2
#from urllib.request import urlopen


userinput = str(input('What character to search for?'))
# url = 'https://swapi.co/api/people/?search=%s'% userinput
url = 'https://swapi.co/api/people/?search=' + userinput
r = requests.get(url) #api command to get data from URL; is this always the first step?
data = r.json() #formatting data into json

# print (data) #will give us entire dictionary object
"""
url2 = 'https://swapi.co/api/planets/1/' # testing URL for 1 planet
r = requests.get(url2)
data2 = r.json()
print (data2)
print (data2['name']) #this works
"""
# Goal: have the computer just print "Name: R2-D2"

def homeworld(homeworldurl):
    r2 = requests.get(homeworldurl)
    data2 = r2.json()
    return data2['name']

def filmname(filmsurl): # pass in a list of URL's
    result = []
    for m in filmsurl: # each individual link
        r3 = requests.get(m)
        data3 = r3.json()
        result.append(data3['title'])
    return result

results = data['results']
for i in results:
    #homeworldurl = i['homeworld']
    homeworldName = homeworld(i['homeworld'])
    filmName = filmname(i['films'])
    # filmsurl = i['films']
    print (i['name']) # datatype: string
    print (homeworldName)
    print (filmName)

# open homeworld url; get name of homeworld
# function to print homeworld
# function to print films


    
    
    
"""
    # try to ge characters in the film
   for z in data3['characters']: #access list of characters; z represents e/ character's URL
        r4 = requests.get(z)
        data4 = r4.json()
        print (data4['name']) #this function just iterates through the last movie
"""
        

"""
r3 = requests.get(filmsurl)
data3 = r3.json()
print (data3)
"""




"""
# Homework: Update this code so that the user can search for any string within
# a character's name. Do this by asking the user for input and updating the URL
# accordingly.

# Make sure to print out the names of all of the matching characters

# Bonus: print the name of the character's homeworld below their name

# Double bonus: print the name(s) of all of the films the character was in
# below their name

# raw input for end of URL?
"""
"""
>>> import urllib.request
>>> import urllib.parse
>>> params = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
>>> url = "http://www.musi-cal.com/cgi-bin/query?%s" % params
>>> with urllib.request.urlopen(url) as f:
...     print(f.read().decode('utf-8'))
...
"""
# https://docs.python.org/3/library/urllib.request.html#urllib-examples

curl https://newsapi.org/v2/everything -G \
    -d q=rideOS \
    -d from=2017-08-11 \
    -d sortBy=popularity \
    -d apiKey=ea2a4ec8eee0414589d6711ddfdcfab0

