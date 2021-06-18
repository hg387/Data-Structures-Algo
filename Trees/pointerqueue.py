#!/usr/bin/env python

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None

    def set_next(self, x):
        self.next_node = x

    def get_next(self):
        return self.next_node


class Queues:
    def __init__(self, current=None, head=None):
        self.head = head
        self.current = current

    # returns the first element on queue Q
    def front(self):
        return self.head.data

    # Inserts the element with data at the end of queue
    def enqueue(self, data):
        x = Node(data)

        if self.current == None:
            self.head = x
            self.current = x
        else:
            self.current.set_next(x)
            self.current = x

    # deletes the first element of queue
    def dequeue(self):
        self.head = self.head.get_next()

    # makes queue empty
    def makenull(self):
        self.head = None
        self.current = None

    # returns true if queue is empty
    def empty(self):
        if self.head == None:
            return True
        else:
            return False









