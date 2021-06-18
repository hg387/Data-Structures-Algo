#!/usr/bin/env python
import sys
# this program is used to evaluate the postfix expression
# stack is used to keep count of operands
# NOTE: make file is not possible to neglect character * which is part of the program
# Because of this condition, I have to hard code the input into the make file
class stack:
    def __init__(self):
        self.L = []

    def push(self,data):
        self.L.insert(0,data)

    def peek(self):
        return self.L[0]

    def delete(self):
        self.L.pop(0)

    def empty(self):
        if len(self.L) == 0:
            return True
        else:
            return False

# exp is in format of list
# to check for the operators
temp = ['+' , '-' , '/' , '*']


def postfix(exp):
    a = stack()
    for i in exp:
        if i not in temp:
            a.push(i)
        else:
            if i == '+':
                x1 = a.peek()
                a.delete()
                x2 = a.peek()
                a.delete()
                a.push(int(x1)+int(x2))
            elif i == '-':
                x1 = a.peek()
                a.delete()
                x2 = a.peek()
                a.delete()
                if (int(x1) >= int(x2)):
                    a.push(int(x1)-int(x2))
                else:
                    a.push(int(x2) - int(x1))
            elif i == '/':
                x1 = a.peek()
                a.delete()
                x2 = a.peek()
                a.delete()
                if (int(x1) >= int(x2)):
                    a.push(int(x1)/int(x2))
                else:
                    a.push(int(x2) / int(x1))
            elif i == '*':
                x1 = a.peek()
                a.delete()
                x2 = a.peek()
                a.delete()
                a.push(int(x1)*int(x2))

    return a.peek()


#x = []
#x = input("Enter the prefix expression:\n")
#for i in range(1,len(sys.argv)):
#    x.append(sys.argv[i])
x = sys.stdin.read().splitlines()
#x = x.splitlines()
#x = x.split(" ")
#print(x)
print(x[0])

y = postfix(x[0].split(" "))



print(y)

