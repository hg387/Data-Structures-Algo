#!/usr/bin/env python

import timeit
from Pointerlist import *
from Arraylist import *
from Arraystack import *
from Pointerstack import *

# Insertion head for 3 cases
start = timeit.default_timer()
def array():
    x = [None]*500
    for i in range(0,500):
        x.insert(i, i)
stop = timeit.default_timer()
print("Insertion Head standard list:" + str(stop-start) + "\n")


start = timeit.default_timer()
def head_array():
  x = Arraylist()
  for i in range(0,500):
    x.insert(i,i)
stop = timeit.default_timer()
print("Insertion Head arraylist:" + str(stop-start) + "\n")

start = timeit.default_timer()
def head_pointer():
  x = Pointerlist()
  for i in range(0,500):
    x.insert(i,i)
stop = timeit.default_timer()

print("Insertion Head pointerlist:" + str(stop-start) + "\n")

# Insertion tail for all three cases
start = timeit.default_timer()
def array_tail():
    x = [None]*500
    for i in range(0,500):
        x.append(1)
stop = timeit.default_timer()
print("Insertion Tail standard list: " + str(stop - start) +"\n")


start = timeit.default_timer()
def tail_array():
  x = Arraylist()
  for i in range(0,500):
    x.insert(1,x.end())
stop = timeit.default_timer()

print("Insertion Tail arraylist: " + str(stop - start) +"\n")

start = timeit.default_timer()
def tail_pointer():
  x = Pointerlist()
  for i in range(0,500):
    x.insert(1,x.end())
stop = timeit.default_timer()

print("Insertion Tail Pointerlist: " + str(stop - start) +"\n")

# Transversal operation for three cases
start = timeit.default_timer()
def transversal_std_array():
    x = [None]*500
    for i in range(0,500):
        new = x[i]

stop = timeit.default_timer()
print("Transversal standard list: " + str(stop - start) +"\n")


start = timeit.default_timer()
def transversal_array():
  x = Arraylist()
  for i in range(0,500):
    x.insert(1,x.end())
  element = x.first()
  while element:
    element = x.Next(element)
stop = timeit.default_timer()

print("Transverse arraylist: " + str(stop - start) +"\n")

start = timeit.default_timer()
def transversal_pointer():
  x = Pointerlist()
  for i in range(0,500):
    x.insert(1,x.end())
  element = x.first()
  while element:
    element = x.Next(element)
stop = timeit.default_timer()

print("Transverse Pointerlist: " + str(stop - start) +"\n")

# Deletion operation for three cases
start = timeit.default_timer()
def std_deletehead():
    x = [None]*500
    for i in range(0,500):
        del x[0]
stop = timeit.default_timer()
print("Delete head standard list: " + str(stop - start) +"\n")

start = timeit.default_timer()

def deletehead_array():
  x = Arraylist()
  for i in range(0,500):
    x.insert(1,x.first())
  for i in range(0,500):
    x.delete(0)
stop = timeit.default_timer()

print("Delete head arraylist: " + str(stop - start) +"\n")

start = timeit.default_timer()
def deletehead_pointer():
  x = Pointerlist()
  for i in range(0,500):
    x.insert(1,x.first())

  for i in range(0,500):
    x.delete(0)
stop = timeit.default_timer()

print("Delete head Pointerlist: " + str(stop - start) +"\n")

# delete tail operation for three cases
start = timeit.default_timer()
def std_listdelete():
    x=[None]*500
    for i in range(0,500):
        del x[-1]
stop = timeit.default_timer()
print("Delete tail standard list: " + str(stop - start) +"\n")


start = timeit.default_timer()
def deletetail_array():
  x = Arraylist()
  for i in range(0,500):
    x.insert(1,x.end())

  for i in range(0,500):
    x.delete(0)
stop = timeit.default_timer()

print("Delete tail arraylist: " + str(stop - start) +"\n")

start = timeit.default_timer()
def deletetail_pointer():
  x = Pointerlist()
  for i in range(0,500):
    x.insert(1,x.end())

  for i in range(0,500):
    x.delete(0)
stop = timeit.default_timer()

print("Delete head Pointerlist: " + str(stop - start) +"\n")

# push operation in all three cases
start = timeit.default_timer()
def array_stdstack():
  x = []
  for i in range(0,500):
    x.append(i)
stop = timeit.default_timer()

print("Push arraystack: " + str(stop - start) +"\n")


start = timeit.default_timer()
def array_pushstack():
  x = Arraystack()
  for i in range(0,500):
    x.push(i)
stop = timeit.default_timer()

print("Push arraystack: " + str(stop - start) +"\n")

start = timeit.default_timer()
def pointer_pushstack():
  x = Pointerstack()
  for i in range(0,500):
    x.push(i)
stop = timeit.default_timer()
print("Push pointerstack: " + str(stop - start) +"\n")

# Pop elements operation in three cases
start = timeit.default_timer()
def stdarray_popstack():
  x = []
  for i in range(0,500):
    x.append(i)
  for i in range(0,500):
    x.pop()
stop = timeit.default_timer()
print("Pop standard list: " + str(stop - start) +"\n")



start = timeit.default_timer()
def array_popstack():
  x = Arraystack()
  for i in range(0,500):
    x.push(i)
  for i in range(0,500):
    x.pop()
stop = timeit.default_timer()
print("Pop arraylist: " + str(stop - start) +"\n")

start = timeit.default_timer()
def pointer_popstack():
  x = Pointerstack()
  for i in range(0,500):
    x.push(i)
  for i in range(0,500):
    x.pop()
stop = timeit.default_timer()
print("Pop Pointerlist: " + str(stop - start) +"\n")
