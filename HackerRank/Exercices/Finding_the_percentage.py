#https://www.hackerrank.com/challenges/finding-the-percentage

from decimal import Decimal

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    student_scores = student_marks[query_name]
    total = sum(student_scores)
    number_of_notes =  len(student_scores) 
    
    avg = Decimal(total / number_of_notes)
    
    print(round(avg,2))
        
    
    
    
