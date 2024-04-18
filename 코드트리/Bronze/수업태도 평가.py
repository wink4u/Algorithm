import sys
from collections import defaultdict

N = int(input())
student = defaultdict(int)
score = defaultdict(list)

for _ in range(N):
    st, sc = input().split()
    student[st] += int(sc)

student_items = list(student.items())
student_items.sort(key = lambda x : x[1])

for i in range(len(student_items)):
    score[student_items[i][1]].append(student_items[i][0])

if len(student_items) != 7:
    min_score = student_items[0][1]

    if len(score[min_score]) == 1:
        print(student_items[0][0])
    else:
        print('Tie')
else:
    score_items = list(score.items())
    score_items.sort(key = lambda x : x[0])

    if len(score_items) == 1:
        print('Tie')
    else:
        if len(score_items[1][1]) == 1:
            print(score_items[1][1][0])
        else:
            print('Tie')
