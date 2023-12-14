import regex as re
import numpy as np
input = open("day3\short-input.txt", "r")

# array = np.loadtxt("short-input.txt", dtype='str', delimiter='')
# print(array)

lst = []
for x in input:
    lst.append(list(x.rstrip()))



print(np.array(lst))


for i,x in enumerate(lst):
    print(i,x)
    for j,y in enumerate(x):
        print(j,y)
