import sys
input = sys.stdin.readline

N, K = map(int, input().split())

block = [0 for _ in range(N + 1)]

for _ in range(K):
    S, E = map(int, input().split())
    block[S - 1] += 1
    block[E] -= 1


for i in range(1, len(block)):
    block[i] += block[i - 1]

block = sorted(block[0:N])

print(block[N // 2])