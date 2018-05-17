"""We begin by assuming that a list with one item (position 00) is already
sorted. On each pass, one for each item 1 through n−1n−1, the current item
is checked against those in the already sorted sublist. As we look back into '
the already sorted sublist, we shift those items that are greater to the right.
When we reach a smaller item or the end of the sublist, the current item can be
inserted.

Figure 5 shows the fifth pass in detail. At this point in the algorithm,
a sorted sublist of five items consisting of 17, 26, 54, 77, and 93 exists.
We want to insert 31 back into the already sorted items. The first comparison
against 93 causes 93 to be shifted to the right. 77 and 54 are also shifted.
When the item 26 is encountered, the shifting process stops and 31 is placed
in the open position. Now we have a sorted sublist of six items."""

a = [4,3,6,1]

def insertion(a):
    # finallist = [] # container for the final list if needed
    interim = a[0]
    for i in range(1,len(a)): # run outerloop len(a)-1 times
        position = i
        print (a)
        while a[position]< a[position-1] and position > 0: # look at #'s up until i; make sure sorted
            print (position)
            interim = a[position-1]
            a[position-1] = a[position]
            a[position] = interim
            position -= 1
            print (a)
    return a
print (insertion(a))
"""
1st run:
i = 1
position = 1
a[1] = 3; a[0] = 4
interim = 4
a[0] = 4
a[1] = 3
position = i-1 --> hm..

2nd run:
i = 2
position = 2
a[2] = 6
a[1] = 4
while loop doesn't execute since placement is correct

3rd run:
i = 3
position = 3
a[3] = 1
a[2] = 6
while loop executes
interim = 6
a[3] = 6
a[2] = 1
[3,4,1,6] (keeps going)

# 1st loop: [3,4,6,1,9,10,5] swap 3 & 4
# 2nd loop: [3,4,6,1,9,10,5] 4 & 6 stay same
# 3rd loop: [3,4,1,6,9,10,5] 1 needs to go to front of list
# as long as a[i] - next # right outside sublist - is greater than a[j]; it can stay put
