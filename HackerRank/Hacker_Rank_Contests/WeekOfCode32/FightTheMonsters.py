#https://www.hackerrank.com/contests/w32/challenges/fight-the-monsters
#!/bin/python3

import sys

def getMaxMonsters(n, hit, t, h):
    numberOfSeconds = 0
    numberOfMonsterKilled = 0 
  
    while numberOfSeconds < t:
        h.sort()   
        h[0] -= hit
        if h[0] <= 0:
            numberOfMonsterKilled += 1
            h.pop(0)
        numberOfSeconds += 1
    return numberOfMonsterKilled
        

n, hit, t = input().strip().split(' ')
n, hit, t = [int(n), int(hit), int(t)]
h = list(map(int, input().strip().split(' ')))
result = getMaxMonsters(n, hit, t, h)
print(result)

