import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 1e9

for i in range(2 << (n - 1)):
    s, b = 1, 0
    for j in range(n):
        if i & (1 << j):
            s *= arr[j][0]
            b += arr[j][1]

    if b != 0:
        answer = min(answer, abs(b - s))

print(answer)