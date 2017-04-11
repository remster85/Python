#https://www.hackerrank.com/contests/w31/challenges/beautiful-word
#!/bin/python3

import sys

isbeautiful = True
voyels = { 'a','e','i','o','u','y'}
w = input().strip()
# Print 'Yes' if the word is beautiful or 'No' if it is not.

for letter in w:

    if letter == lastletter:
        isbeautiful = None
        break 

    if letter in voyels:
        if wasLastLetterAVoyel:
            isbeautiful = None
            break
        wasLastLetterAVoyel = True        
    else:
        wasLastLetterAVoyel = None 
        
    lastletter = letter
    
    
if isbeautiful:
    print('Yes')
else:
    print('No')
    
