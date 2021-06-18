#!/usr/bin/env python
from lcrstree import *

# TESTER PROGRAM:
print("create2 testing\n")
print("creating a tree with the root to be '0' and children to be '1' and '2'\n")
temp = create2(0,create2(1,None,None),create2(2,None,None))
print("Parent printed predicted to be 0\n")
print(temp.leftmost_child().parent(),"is parent with label:",temp.leftmost_child().parent().label())
print("left most child tested predicted to be 1\n")
print(temp.leftmost_child(),"is left most child with label:",temp.leftmost_child().label())
print("right sibling tested predicted to be 2\n")
print(temp.leftmost_child().right_sibling(),"is right sibling with label:",temp.leftmost_child().right_sibling().label())
print("label tested predicted to be 0\n")
print(temp.label())
print("Testing the root of the tree\n")
print(temp.root())
print("making the tree null\n")
temp.makenull()
print("checking if tree is null or not by printing the parent of the tree\n")
print(temp.parent())
print("Testing Ended Successfully!!\n")