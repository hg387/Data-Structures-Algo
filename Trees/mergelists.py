#!/usr/bin/env python
from listconcat import *

# This program is merging and sorting the lists
# To run this program correctly, you need to have listconcat.py from Programming Assignment2 which I have also included with this assignment
# Also, this program is printing the result in the end

def insertion_sort(old):
    # looping through the whole list
    for i in range(1,old.pointer):
        # for keeping the count of the elements
        count  = old.L[i]
        # counter of i
        counter = i - 1
        # moving elements 
        while counter >= 0 and count < old.L[counter]:
            old.L[counter+1] = old.L[counter]
            counter = counter - 1

        old.L[counter+1] = count

    return old


# TEST FOR THE PROGRAM
a = Arraylist()
a.insert(1, 0)
a.insert(2, 1)
a.insert(3, 2)
a.insert(4, 3)

b = Arraylist()
b.insert(5, 0)
b.insert(6, 1)
b.insert(7, 2)
b.insert(8, 3)

c = Arraylist()
c.insert(9, 0)
c.insert(10, 1)
c.insert(11, 2)
c.insert(12, 3)

d = Arraylist()
d.insert(13, 0)
d.insert(14, 1)
d.insert(15, 2)
d.insert(16, 3)

lists = Arraylist()
lists.insert(a,0)
lists.insert(d,1)
lists.insert(b,2)
lists.insert(c,3)

# calling the concatenate function to join all the lists
x = con(lists)
# calling the merge function to sort list
x = insertion_sort(x)

# printing the result
# Expected result to be [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(x.L[0:x.pointer])


