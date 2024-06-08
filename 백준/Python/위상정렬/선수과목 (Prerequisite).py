import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
# 과목의수, 선수 조건의 수

node = [0] * (N + 1)

check = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    check[a].append(b)
    node[b] += 1

ans = [1] * (N + 1)

def topology_sort():
    res = []
    q = deque()

    for i in range(1, N + 1):
        if node[i] == 0:
            q.append(i)
            ans[i] = 1

    for i in range(1, N + 1):
        now = q.popleft()
        res.append(now)

        for next in check[now]:
            node[next] -= 1
            if node[next] == 0:
                q.append(next)
            ans[next] = ans[now] + 1

    print(*ans[1:])

topology_sort()
