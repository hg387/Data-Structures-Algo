#!/usr/bin/env python

# Do not get confused with the naming Node
# it is just like cell mentioned in the book

class Arraystack:
    def __init__(self, size=1000, head=0):
        self.size = size
        self.head = head
        self.L = [None] * (self.size)

    # pushing the element on the top of the stack
    def push(self, data):
        self.L[self.head] = data
        self.head = self.head + 1

    # returns the element on the top the stack
    def top(self):
        if (self.head == 0):
            print("Arraystack empty")
        else:
            return self.L[self.head - 1]

    # delete the top element of the stack
    def pop(self):
        if (self.head == 0):
            print("Arraystack empty")
        else:
            self.head = self.head - 1
            self.L[self.head] = None

    # return True if stack is empty, otherwise return False
    def empty(self):
        if (self.head) == 0:
            return True
        else:
            return False

    # emptying the stack
    def makenull(self):
        self.size = 0
        self.head = 0

