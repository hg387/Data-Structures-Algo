#!/usr/bin/env python
from Arraylist import *

# This program is concatenating the lists (Array lists used in programming assignment 1)
# To run this program correctly, you need to have Arraylist.py from Programming Assignment1 which I have also included with this assignment
# Also, this program is printing the result in the end

def con(lists):
    temp = Arraylist()
    # empty list for concatenating the lists

    count_index = 0 # for keeping track of new indexes
    # looping over the list elements
    for i in range(0,lists.pointer):
        count = lists.L[i]

        # looping the the actual lists that needed to concatenate
        for i in range(0,count.pointer):
            temp.insert(count.L[i],i+count_index) # inserting elements in temp list

        count_index += count.pointer # updating the new indexes count

        # returning the new list
    return temp


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
lists.insert(b,1)
lists.insert(c,2)
lists.insert(d,3)

# calling the concatenate function
x = con(lists)
# printing the result
# Expected result to be [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
#print(x.L[0:x.pointer]) #for printing purpose, remove the # comment to print the result
