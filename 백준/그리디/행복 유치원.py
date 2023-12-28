import sys
input = sys.stdin.readline

N, K = map(int, input().split())

students = list(map(int, input().split()))

temp = []

for i in range(N - 1):
    temp.append(students[i + 1] - students[i])

temp.sort()
result = 0

for i in range(N - K):
    result += temp[i]

print(result)