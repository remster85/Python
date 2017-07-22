#https://www.hackerrank.com/challenges/no-idea

input()
seeds = input().split(' ')
goodSeeds = set(input().split(' '))
badSeeds = set(input().split(' '))

happinessLevel = 0

for seed in seeds:

    if seed in goodSeeds:
        happinessLevel+= 1
        
    if seed in badSeeds:
        happinessLevel-=1
         
print(happinessLevel)
