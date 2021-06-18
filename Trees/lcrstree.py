#!/usr/bin/env python


class Node:
    def __init__(self,data=None):
        self.left = None # left child
        self.right = None # right child
        self.data = data # label of the node
        self.parent_id = None # parent of the node

    # returns the label of the root node
    def label(self):
        return self.data

    # returns the parent of the node
    def parent(self):
        return self.parent_id

    # returns the left most child
    def leftmost_child(self):
        return self.left

    # returns the right sibling
    def right_sibling(self):
        if self.right != None:
            return self.right
        else:
            return Node()

    # making the tree null
    def makenull(self):
        self.left = None
        self.right = None
        self.data = None
        self.parent_id = None

    # returning the root of the tree
    def root(self):
        temp = self
        while temp.parent_id != None:
            temp = temp.parent_id

        return temp

# connecting two trees
#I have used less space but more time if we put in the right-sibling
#field of the rightmost child a pointer to the parent, in place of the null pointer that
#would otherwise be there

def create2(v,T1,T2):
    if (T1 == None) and (T2 == None):
        Tree = Node()
        Tree.data = v

    elif (T1 != None) and (T2 != None):
        Tree = Node()
        Tree.data = v
        Tree.left = T1
        Tree.left.parent_id = Tree

        (Tree.left).right = T2
        (Tree.left).right.parent_id = Tree
    else:
        print("error in arguments, please check them\n")

    return Tree









