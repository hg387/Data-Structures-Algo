#!/usr/bin/env python
# configuring the level order using pointer tree
from lcrstree import *


def levelorder(tree):
	temp = []
	count = tree.root()

	temp.append(count)

	while(len(temp) > 0):
		print(temp[0].label())
		node = temp.pop(0)

		if node.left is not None:
			temp.append(node.left)
		if node.right is not None:
			temp.append(node.right)

# Tree shape
# Printed the tree in order of a,b,c,d,e,f,g
#			a
#		/		\
#		b		  c
#	  /  \	    /	\
#	 d    e     f    g

T1 = Node("b")
T1.left = Node("d")
T1.right = Node("e")

T2 = Node("c")
T2.left = Node("f")
T2.right = Node("g")

T = create2("a",None,None)
T.left = T1
T.right = T2

levelorder(T)
