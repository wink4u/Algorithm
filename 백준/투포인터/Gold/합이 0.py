import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
student = list(map(int, input().split()))
student.sort()
student_cnt = Counter(student)
res = 0
for i in range(N):
    value = student[i]
    start, end = i + 1, N - 1

    while start < end:
        check_value = value + student[start] + student[end]

        if check_value < 0:
            start += 1
        elif check_value == 0:
            if student[start] == student[end]:
                res += end - start
            else:
                res += student_cnt[student[end]]
            start += 1
        else:
            end -= 1

print(res)