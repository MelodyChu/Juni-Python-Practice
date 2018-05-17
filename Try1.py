
def my_list_function(stuff):
	result=[]
	for x in stuff:
   		if not (x.startswith("S") or
   		x.startswith("d") or
   		len(x)>4):
			result.append(x)
	return result

my_list_function(["home","cat","Soup","coffee"])

print my_list_function(["home","cat","Soup","coffee"])

## Next attempt

list_name = ["home", "cat", "Soup", "coffee", "Sorry"]
def list_of_words(stuff):
  result = []
  for word in stuff:
    if word[:1] !="S" and word[:1] !="d" and len(word) <= 4:
      result.append(word)
  return result
print list_of_words(list_name)