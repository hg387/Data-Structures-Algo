#!/usr/bin/env python
# This program is for tree array implementation
class Node:
    def __init__(self,data=None):
        self.data = data
        self.L = []
        self.parent_id = None

    # empty the tree
    def makenull(self):
        self.data = None
        self.L = []
        self.parent_id = None

    # returns the parent of the node
    def parent(self):
        return self.parent_id

    # returns the root of the node
    def root(self):
        temp = self
        while temp.parent_id != None:
            temp = temp.parent_id
        return temp

    # returns the leftmost child of the tree
    def leftmost_child(self):
        return self.L[0]

    # returns the data of the node
    def label(self):
        return self.data

    # returns the right sibling of the node
    def right_sibling(self):
        # calculating the index then adding the +1 to find the right most node
        try:
            return self.parent_id.L[(self.parent_id.L.index(self))+1]
        except IndexError:
            return Node()

def createi(v,*argv):
    if len(argv) >= 4:
        print("No. of arguments are not correct\n")
    else:
        temp = Node()
        temp.data = v
        for arg in argv:
            temp.L.append(arg)
            arg.parent_id = temp
        return temp






