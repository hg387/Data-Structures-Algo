#!/usr/bin/env python

from Pointerstack import *

print("Testing Pointerstack begins here: \n")
print("initializing new stack\n")
a = Pointerstack()
print("pushing five elements into the stack\n")
print("elements are 1,2,3,4,5\n")
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
print("printing the top of the stack i.e 5")
print(a.top())

print("\nremoving 2 elements from the top, resulting top to be 3\n")
a.pop()
a.pop()
print("new top would be 3\n")
print(a.top())

print("removing the rest 3 elements make it null\n")

a.pop()
a.pop()
a.pop()

print("empty() should return true:\n")
print(a.empty())

print("\n adding some elements to test makenull fuctionality\n")

a.push(1)
a.push(2)
a.makenull()

print("makenull function executed check for top():\n")

a.top()
