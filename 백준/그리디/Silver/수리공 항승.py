import sys
input = sys.stdin.readline

N, L = map(int, input().split())

pipe = list(map(int, input().split()))
pipe.sort()

st = pipe[0] - 0.5
count = 1

for i in range(1, N):
    if pipe[i] + 0.5 <= st + L:
        continue
    else:
        count += 1
        st = pipe[i] - 0.5

print(count)