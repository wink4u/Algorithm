import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())

alpha = ['A', 'C', 'G', 'T']

check = [[0, 0, 0, 0] for _ in range(M)]

for i in range(N):
    code = input().strip()

    for j in range(M):
        check[j][alpha.index(code[j])] += 1

res_alpha = ''
res_value = 0
for i in range(M):
    max_v = max(check[i])
    for j in range(4):
        if check[i][j] == max_v:
            res_alpha += alpha[j]
            break

    res_value += N - max_v

print(res_alpha)
print(res_value)