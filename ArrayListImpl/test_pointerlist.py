#!/usr/bin/env python

from Pointerlist import *

print("Testing Pointer list begins here:")
print("creating a new Pointer list\n")
a = Pointerlist()
print("Head Inserting 4 elements in the list [1,2,3,4]\n")

a.insert(1, 0)
a.insert(2, 1)
a.insert(3, 2)
a.insert(4, 3)

print("Printing the list as [1,2,3,4]\n")
a.printlist()

print("\nGetting the first element of the list\n")
print(a.first())

print("\nGetting the last element of the list\n")
print(a.end())

print("\nPrinting the element at index 0 which would be 1\n")
print(a.retrieve(0))

print("\nPrinting the index of the element 2 that is 2\n")
print(a.locate(2))

print("\n Deleting the element at index 2\n")
a.delete(2)

print("Printing new list which would be [1,2,4]\n")
a.printlist()

print("\nlet's locate the index of 4 in our list\n")
print(a.locate(4))

print("\n next element to the index 0 i.e 2\n")
print(a.Next(0).get_data())

print("\n previous element to the index 1 i.e 1\n")
print(a.previous(1).get_data())

print("making list it null\n")
a.makenull()
print(a.end())
