import re
numberofcases = int(input())
i = 0
while i < numberofcases:
    n = input()
    try:
        float(n)
        if not '.' in str(n):
            print("False")
        else:
            print("True")
    except:
        print("False")
    i = i + 1
