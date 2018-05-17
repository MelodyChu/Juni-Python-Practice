"""
a = 0
def test_square_root(a):
    while a < 10:
        a += 1
        print (a)
    return   
print (test_square_root(a))
"""
    
"""
for a in range(1,10):
    print (a)
"""
"""Write a function called is_sorted that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise. You can assume (as a precondition) that the elements of the list can be compared with the relational operators <, >, etc.
For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) should return False."""
"""
list1 = [4,6,10,11]
def is_sorted(list1):
    for i in range(0,len(list1)-1): # i is index of list
        if list1[i+1] < list1[i]: # if index of num to right is > than index of num to left 
            return False
    return True
print (is_sorted(list1))
"""
"""
Two words are anagrams if you can rearrange the letters
from one to spell the other. Write a function called is_anagram
that takes two strings and returns True if they are anagrams.
a = 'silent'
b = 'listen'
def is_anagram(a,b):
    count_same = 0 #counting number of times letters = e/ other; if this number = length of word, then true
    for i in a: # outerloop - iterate through all letters of a
        for j in b: #innerloop - iterate through all letters of b
            if i == j: #if letters = each other
                count_same += 1 #how to make this go back to top of loop
    if count_same >= len(a) and len(a) == len(b): #count_same == len(b)
        return True
    else:
        return False
print (is_anagram(a,b))
"""   
"""
list1 = [1,3,5,6,0,1]
def find_dup(list1):
    count = 1 #counting the # of times one thing shows up
    for i in range(0, len(list1)):
        for j in range(0, len(list1)):
            if list1[i] + list1[j] == 0 and i != j: #if list #'s are same but indexes are not the same
                return True
    else:
        return False

print (find_dup(list1))
"""
"""
list1 = [1,3,5,6,0,1]
def remove_dup(list1):
    newlist = []
    for i in list1:
        if i not in newlist:
            newlist.append(i)
    return newlist
print (remove_dup(list1))

def set_dup(list1):
    newlist = set(list1)
    return newlist
print (set_dup(list1))
"""
#finding reverse pairs
lista = ['cat','silent','sweater','listen','tac']
def find_reverse(lista):
    results = []
    for i in lista: #i is word in lista
        print ("top of loop")
        z = 0 #is is iterator through the index of letters in word
        
        for j in lista: #j is word in lista
            if i != j and i[z] == j[len(j)-(z+1)]:
                z += 1
                print (z)
        results.append(i)
        results.append(j)
    return False
print (find_reverse(lista))
# cat
        
