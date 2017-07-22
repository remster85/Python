#!/bin/python3

import sys

n = 7
p = 5
numberOfPagesTurned = 0

if p > n/2:
    currentpage = n
    while currentpage != p and currentpage-1 != p:
        numberOfPagesTurned = numberOfPagesTurned + 1
        currentpage = currentpage - 2
        #print (numberOfPagesTurned)
        #print (currentpage)

else:
    currentpage = 1
    if p != currentpage:
        numberOfPagesTurned = numberOfPagesTurned + 1
        while currentpage != p and currentpage + 1 != p:
            numberOfPagesTurned = numberOfPagesTurned + 1
            currentpage = currentpage+2
            #print (numberOfPagesTurned)
            #print (currentpage)


sys.stdout.write(str(numberOfPagesTurned))

# your code goes here
