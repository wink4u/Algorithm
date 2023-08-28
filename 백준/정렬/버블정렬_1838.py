import sys
input = sys.stdin.readline

N = int(input())
line = list(map(int, input().split()))
pre_line = dict()
after_line = dict()

for i in range(N):
    pre_line[line[i]] = i

line.sort()

for i in range(N):
    after_line[line[i]] = i

max_v = 0
for i in pre_line:
    max_v = max(pre_line[i] - after_line[i], max_v)

print(max_v)

