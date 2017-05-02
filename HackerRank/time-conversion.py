#https://www.hackerrank.com/challenges/time-conversion/
#!/bin/python3

import sys

time = input().strip()
timesplits = time.split(':')

AMorPM = time[-2:]
hours = timesplits[0]
minutes = timesplits[1]
seconds = timesplits[2][0:2]

if AMorPM == 'PM':
    if hours != '12':
        hours = int(hours) + 12
else:
    if hours == '12':
        hours = '00'
    

    
print('{0}:{1}:{2}'.format( hours, minutes, seconds))
