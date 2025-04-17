import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def dfs(now):
    visit[now] = 1
    bomb = 0

    for nxt, value in node[now]:
        if not visit[nxt]:
            bomb += min(value, dfs(nxt))

    return bomb if bomb else 1e6


for _ in range(t):
    n, m = map(int, input().split())

    if n == 1:
        print(0)
    else:
        node = [[] for _ in range(n + 1)]
        visit = [0] * (n + 1)

        for _ in range(m):
            a, b, w = map(int, input().split())
            node[a].append([b, w])
            node[b].append([a, w])


        print(dfs(1))