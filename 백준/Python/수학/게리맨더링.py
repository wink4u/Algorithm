import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nodes = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    _, *node = map(int, input().split())

    for v in node:
        nodes[i][v - 1] = 1

def bfs(nd):
    q = deque()
    check = [0 for _ in range(N)]
    q.append(nd[0])
    check[nd[0]] = 1

    while q:
        nq = q.popleft()

        for t in range(len(nodes[nq])):
            if nodes[nq][t] == 0:
                continue
            if t not in nd:
                continue
            if not check[t]:
                check[t] = 1
                q.append(t)

    return check.count(1) == len(nd)


def total(nds):
    res = 0
    for nd in nds:
        res += nums[nd]

    return res


X = {i for i in range(N)}
ans = int(1e9)

for i in range(1, N // 2 + 1):
    AC = tuple(combinations(X, i))

    for A in AC:
        B = list(X.difference(A))

        if bfs(A) and bfs(B):
            a_res = total(A)
            b_res = total(B)
            ans = min(ans, abs(a_res - b_res))

if ans == int(1e9):
    print(-1)
else:
    print(ans)
