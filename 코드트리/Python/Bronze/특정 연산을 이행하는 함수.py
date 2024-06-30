import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

arr = []

for i in (a, b, c):
    tmp = 0
    if i % 2:
        tmp = i * 3 - 20
    else:
        tmp = i // 2

    arr.append(tmp)

print(*arr)