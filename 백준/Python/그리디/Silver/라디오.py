import sys
input = sys.stdin.readline

A, B = map(int, input().split())

N = int(input())

res = abs(A - B)

for _ in range(N):
    num = int(input())
    res = min(res, abs(num - B) + 1)

print(res)