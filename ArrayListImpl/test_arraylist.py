#!/usr/bin/env python

from Arraylist import *


print("testing Arraylist begins here:")
print("creating a new Arraylist\n")
a = Arraylist()
print("Head Inserting 4 elements in the list [1,2,3,4]\n")

a.insert(1 ,0)
a.insert(2 ,1)
a.insert(3 ,2)
a.insert(4 ,3)

print("Printing the list as [1,2,3,4]\n")
print(a.L[:a.pointer])

print("\nGetting the first position of the list\n")
print(a.first())

print("\nGetting the last position of the list\n")
print(a.end())


print("\nPrinting the element at index 0 which would be 1\n")
print(a.retrieve(0))

print("\nDeleting the elemet at index 2\n")
a.delete(2)

print("Printing new list which would be [1,2,4]\n")
print(a.L[:a.pointer])

print("\nlet's locate the index of 4 in our list\n")
print(a.locate(4))

print("\n next position to the index 0 i.e 1\n")
print(a.Next(0))

print("\n previous position to the index 1 i.e 0\n")
print(a.previous(1))

print("making list null\n")
a.makenull()
print("printing the end element of the empty list i.e 0\n")
print(a.first())