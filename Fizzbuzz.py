for i in range(1,51):
  if i % 3 == 0 and i % 5 == 0: # checking to see if # is multiple of 3 & 5
    print ("Fizzbuzz")
  elif i % 5 == 0:
    print ("Buzz")
  elif i % 3 == 0:
    print ("Fizz")
  else:
    print (i)
