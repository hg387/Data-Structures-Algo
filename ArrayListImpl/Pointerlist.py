#!/usr/bin/env python

# Do not get confused with the naming Node
# it is just like cell mentioned in the book
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None

    def set_next(self, Node):
        self.next_node = Node

    def get_next(self):
        return self.next_node

    def get_data(self):
        return self.data


class Pointerlist:
    def __init__(self, current=None, start=None):
        self.current = current
        self.start = start
        self.count = 0

    # returns the first element of the list
    def first(self):
        if self.start == None:
            return None
        else:
            return ((self.start).get_data())

    # returns the last element of the list
    def end(self):
        if self.start == None:
            print("list is empty")
        else:
            counter = self.start
            while (counter.get_next() != None):
                counter = counter.get_next()
            return ((counter).get_data())

    # Insert the data at the position
    def insert(self, data, position):
        x = Node(data)
        if (position == 0 and self.start == None):
            self.start = x
            self.current = x
            self.count = 1
        elif (position == self.count):
            self.count = self.count + 1
            self.current.set_next(x)
            self.current = x
        elif (position < self.count):
            self.count = self.count + 1

            counter = self.start
            temp_fn = 0
            for i in range(0, position - 1):
                counter = counter.get_next()

            temp_fn = counter.get_next()
            counter.set_next(x)
            x.set_next(temp_fn)

        else:
            print("Data not aligned correctly")

    # delete the element at the position
    def delete(self, position):
        counter = self.start
        if (self.start == None):
            print("List empty")
        elif (position == 0):
            self.start = (self.start).get_next()
            self.count = self.count - 1
        elif (position <= self.count):
            self.count = self.count - 1
            for i in range(0, position - 1):
                counter = counter.get_next()
            temp_fn = (counter.get_next()).get_next()
            counter.set_next(temp_fn)

    # returns the data available at the position
    def retrieve(self, position):
        counter = self.start
        if (position > self.count):
            print("position out of size")
        else:
            for i in range(0, position):
                if (counter.get_next() != None):
                    counter = counter.get_next()

        return counter.get_data()

    # returns the index of the data in the list
    def locate(self, data):
        counter = self.start
        count = 0
        while (counter.get_data() != data):
            counter = counter.get_next()
            count = count + 1

        return count

    # returns the pointer to next element of the given position
    def Next(self, position):
        counter = self.start
        if (position > self.count):
            print("position out of size")
        else:
            for i in range(0, position + 1):
                if (counter.get_next() != None):
                    counter = counter.get_next()

            return counter

    # returns the pointer to the previous element of the given position
    def previous(self, position):
        counter = self.start
        if (position == 0 or position > self.count):
            print("position out of size")
        else:
            for i in range(0, position - 1):
                if (counter.get_next() != None):
                    counter = counter.get_next()

            return counter

    # emptying the list, making it null
    def makenull(self):
        self.count = 0
        self.start = None
        self.current = None

    # printing the list for testing purposes
    def printlist(self):
        counter = self.start
        point = 0
        while (counter != None):
            point = point + 1
            print(counter.get_data())
            counter = counter.get_next()
        if (point == 0):
            print("list empty")











