#!/usr/bin/env python

# Do not get confused with the naming Node
# it is just like cell mentioned in the book

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None

    def set_next(self, node):
        self.next_node = node

    def get_next(self):
        return self.next_node

    def get_data(self):
        return self.data


class Pointerstack:
    def __init__(self, size=0, head=None):
        self.size = size
        self.head = head

    # pushing the element on the top of the stack
    def push(self, data):
        x = Node(data)
        if (self.head == None):
            self.head = x
            self.size = self.size + 1
        else:
            self.size = self.size + 1
            tmp = self.head
            self.head = x
            (self.head).set_next(tmp)

    # returns the element at the top of the stack
    def top(self):
        if (self.head == None):
            print("Pointerstack empty")
        else:
            return (self.head).get_data()

    # delete the element at the top of the stack
    def pop(self):
        if (self.head == None):
            print("Pointerstack empty")
        else:
            self.head = (self.head).get_next()
            self.size = self.size - 1

    # if stack is empty return True, otherwise return False
    def empty(self):
        if (self.head) == None:
            return True
        else:
            return False

    # emptying the stack, making it null
    def makenull(self):
        self.size = 0
        self.head = None


