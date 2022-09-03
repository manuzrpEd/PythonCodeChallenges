#List comprehension preferred over for loops
L = [i for i in range (1, 1000) if i%3 == 0]
cube_numbers = [n**3 for n in range(1,10) if n%2 == 1]

# multiple assignments:
a, b, c, d = 2, 3, 5, 7

# concatenate strings:
concatenatedString = " ".join (["Programming", "is", "fun."])

# element in list better than set the list:
for element in L:
    pass

#Don’t construct a set for a conditional.
if element in L:
    pass

# do not use dot operation:
from math import sqrt
val = sqrt(60)

# write code efficiently, exit early:
if (not 1>0) or (not 2>0):
    raise Exception("some error")
pass

# sets and unions before loops:
a = [1,2,3,4,5]
b = [2,3,4,5,6]
overlaps = set(a) & set(b)
print(overlaps)

#https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
#fibonacci sequence