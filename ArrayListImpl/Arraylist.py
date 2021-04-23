#!/usr/bin/env python

# Do not get confused with the naming Node
# it is just like cell mentioned in the book

class Arraylist:
    def __init__(self ,size=1000 ,pointer=0):
        self.size = size
        self.pointer = pointer
        self.L = [None ] *(self.size)

    # returns the position of the first element
    def first(self):
        return 0

    # returns the position of the last element
    def end(self):
        return self.pointer

    # insert the data at given position
    def insert(self ,data, position):
        if (position > self.pointer):
            print("Arraylist out of size")
        elif (position == self.pointer):
            self.L[self.pointer] = data
            self.pointer = self.pointer + 1
        else:
            self.L[position +1:self.pointer +1] = self.L[position:self.pointer]
            self.L[position] = data
            self.pointer = self.pointer + 1

    # delete the element at a given position
    def delete(self ,position):
        if (position > self.pointer):
            print("Arraylist out of size")
        elif(position == self.pointer):
            self.L[position] = None
            self.pointer = self.pointer - 1
        else:
            self.L[position:self.pointer] = self.L[position +1 : self.pointer +1]
            self.pointer = self.pointer - 1

    # retrieve the element at the position
    def retrieve(self ,position):
        if (position > self.pointer):
            return None
        else:
            return self.L[position]

    # returns the index of the data in the list
    def locate(self ,data):
        i = 0
        while (self.L[i] != data) and i <= self.pointer:
            i = i + 1

        if (i > self.pointer):
            print("Data not found")
        else:
            return (i)

    # returns the pointer to next element of the given position
    def Next(self, position):
        if (position + 1 >= self.pointer):
            print("NO possible value")
        else:
            return position + 1

    # returns the pointer to the previous element of the given position
    def previous(self, position):
        if (position == 0 or position > self.pointer):
            print("NO possible value")
        else:
            return position - 1

    # making the list null ,emptying the list
    def makenull(self):
        self.size = 1000
        self.pointer = 0
        self.L = [None ] *(self.size)


