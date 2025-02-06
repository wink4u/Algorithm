import sys
input = sys.stdin.readline

N = int(input())

# 0 - 2 1 - 3 2 - 5 3 - 9
start = 2
for i in range(N):
    plus = start - 1
    start += plus

print(start * start)
