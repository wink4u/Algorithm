import sys
input = sys.stdin.readline

A,B,V = map(int, input().split())

V -= B

day = A - B
res = 0
if V % day:
    res = V // day + 1
else:
    res = V // day

print(res)