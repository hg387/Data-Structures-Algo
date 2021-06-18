#!/usr/bin/env python
from pointerqueue import *

a = Queues()
print("Inserting elements in the queue")
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
print("Printing the front element of the queue")
print(a.front())
print("Deleting (dequeue) the first element of the queue")
a.dequeue()
print("Printing the new front element of the queue")
print(a.front())
print("making the queue null")
a.makenull()
print("checking if the queue is empty now")
print(a.empty())


