import sys

input = sys.stdin.readline

n = int(input())
bead = list(map(int, input().split()))
k = int(input())
check = list(map(int, input().split()))

dp = {bead[0]}

for i in range(1, n):
    s = {bead[i]}
    for j in dp:
        s.add(j + bead[i])
        s.add(abs(j - bead[i]))
    dp = dp | s

print(*map(lambda x: ('Y' if x in dp else 'N'), check))