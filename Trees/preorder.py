
#!/usr/bin/env python
import sys
# this program can be easily done using recursion
# as expression with brackets are not mentioned in the instructions
# so this program does not take expressions with brackets
# exp is in format of list
# NOTE: make file is not possible to neglect character * which is part of the program
# Because of this condition, I have to hard code the input into the make file

def prefix(exp):
    a = exp.pop(0)
    if a == "/":
        return prefix(exp) / prefix(exp)
    elif a == "-":
        return prefix(exp) - prefix(exp)
    elif a == "+":
        return prefix(exp) + prefix(exp)
    elif a == "*":
        return prefix(exp) * prefix(exp)
    else:
        return int(a)


x = sys.stdin.read().splitlines()
print(x[0])

y = prefix(x[0].split(" "))


print(y)




