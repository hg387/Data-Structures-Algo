#!/usr/bin/env python
from loctree import *

#TESTER PROGRAM
print("Creating the tree which has root node labeled '1' and nodes '2', '3', '4'")

T1 = createi('2',Node())
T2 = createi('3',Node())
T3 = createi('4',Node())

T = createi('1',T1,T2,T3)

print("\nRoot for the tree is:",T.root(),"with the label:",T.root().label())

print("\nPrinting all the children with the labels")

for i in T.L:
    print("\nThe child is",i,"with the label",i.label(),"and the parent",i.root())

print("\nPrinting the left_most child")
print("The left_most child is", T.leftmost_child(),"with the label is",T.leftmost_child().label())

new_T = (T.leftmost_child()).right_sibling()
print("\nPrinting the right sibling of left_most sibling")
print("The right sibling of left_most sibling is", new_T,"with the label is",new_T.label())

new_T = new_T.right_sibling()
print("\nPrinting the right sibling of the right sibling")
print("The right sibling of the right sibling is", new_T,"with the label is",new_T.label())

new_T = new_T.right_sibling()
print("\nPrinting the right sibling of the right sibling, Now it should return None")
print("The right sibling of the right sibling is", new_T,"with the label is",new_T.label())

print("\nmaking tree null")
T.makenull()

print("Now checking the parent of the empty tree, it should return None")
print(T.parent())