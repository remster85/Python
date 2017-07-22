#https://www.hackerrank.com/challenges/word-order

from collections import OrderedDict

n = int(input())

i = 0
words = OrderedDict()

while i < n:
    item = input()
    if item in words:
        words[item] += 1
    else:
        words[item] = 1
    i = i + 1    
    
print(str(len(words)) )
for word in words:
    print(str(words[word])+ ' ', end='')
    
