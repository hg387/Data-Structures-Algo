#!/usr/bin/env python

#we make the class for base tree of nodes here
class tree:
	def __init__(self,left,right,parent):
		self.parent = parent
		self.left = left
		self.right = right

#we make the class alphabet here
class alphabet:
	def __init__(self,char,probability,leaf):
		self.char = char
		self.probability = probability
		self.leaf = leaf

#we make the class forest here
class forest:
	def __init__(self,weight,root):
		self.weight = weight
		self.root = root

#make function takes a value for left tree and right tree and returns the counter
def make(ltree,rtree):
	counter = len(TREE)
	TREE.append(tree(0,0,0))

	TREE[counter].left = FOREST[ltree].root
	TREE[counter].right = FOREST[rtree].root

	TREE[counter].parent = 0
	TREE[FOREST[rtree].root].parent = counter
	TREE[FOREST[ltree].root].parent = counter
	return counter

def lightones(one,two):

	if FOREST[0].weight > FOREST[1].weight:
		one =1
		two = 0
	else:
		one = 0
		two = 1

	for i in range(2,len(FOREST)):
		if FOREST[i].weight < FOREST[two].weight:
			two = i
		if FOREST[i].weight < FOREST[one].weight:
			two = one
			one = i

	return (one,two)


def huffman():

	temp1 = 0

	temp2 = 0

	counter_temp = len(FOREST)
#We use the huffman algorithm to obtain the minimum frequency nodes out of the min heap and replace the lowest two by a new node with the lowest two nodes as daughter nodes and repeat this.
	while counter_temp > 1:

		temp1, temp2 = lightones(temp1,temp2)

		new = make(temp1,temp2)

		FOREST[temp1].weight = FOREST[temp1].weight + FOREST[temp2].weight

		FOREST[temp1].root = new

		FOREST[temp2] = FOREST[counter_temp-1]

		del FOREST[counter_temp-1]

		counter_temp = counter_temp - 1

	return



ALPHABET = [alphabet('a',7,0), alphabet('b',9,1), alphabet('c',12,2), alphabet('d',22,3), alphabet('e',23,4), alphabet('f',27,5)]
TREE = [tree(0,0,0), tree(0,0,0), tree(0,0,0), tree(0,0,0), tree(0,0,0), tree(0,0,0)]
FOREST = [forest(7,0), forest(9,1), forest(12,2), forest(22,3), forest(23,4), forest(27,5)]

print("For the first run")
print("TREE would be equal:")
k=0
while(k<len(TREE)):
	print(TREE[k])
	k+=1
print("\n")
k=0
print("ALPHABET would be equal:")
while(k<len(ALPHABET)):
	print(ALPHABET[k])
	k+=1
print("\n")
k=0
print("FOREST would be equal:")
while(k<len(FOREST)):
	print(FOREST[k])
	k+=1
print("\n")

huffman()

print("Result would be:")
print("\n")
print("TREE would be equal:")
k=0
while(k<len(TREE)):
	print(TREE[k])
	k+=1
print("\n")
k=0
print("ALPHABET would be equal:")
while(k<len(ALPHABET)):
	print(ALPHABET[k])
	k+=1
print("\n")
k=0
print("FOREST would be equal:")
while(k<len(FOREST)):
	print(FOREST[k])
	k+=1
print("\n")


