#https://www.hackerrank.com/contests/w31/challenges/accurate-sorting/submissions/code/1301290076
#!/bin/python3

import sys

def isArraySorted(a):
    isArraySorted = True
    for i in range(1,len(a)):
        if a[i] < a[i-1]:
            isArraySorted = None
            break
    return isArraySorted


q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    # Write Your Code Here
  
    previousitem = a[0]
    for i in range(1,len(a)): 
            if a[i] < previousitem:
                buffer = a[i]
                a[i] = previousitem
                a[i-1] = buffer
            previousitem =  a[i]   
            
    if isArraySorted(a):
       print('Yes')
    else:
        print('No')
                  
