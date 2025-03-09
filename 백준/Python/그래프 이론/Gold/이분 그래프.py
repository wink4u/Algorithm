import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    v, e = map(int, input().split())
    node = [[] for _ in range(v + 1)]

    for i in range(e):
        a, b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)

    c = {1 : 2, 2 : 1}

    def bfs():
        visit = [0] * (v + 1)

        for i in range(1, v + 1):
            if not visit[i]:
                q = deque()
                q.append([i, 1])
                visit[i] = 1
                while q:
                    for _ in range(len(q)):
                        now, color = q.popleft()
                        for nxt in node[now]:
                            if not visit[nxt]:
                                visit[nxt] = c[color]
                                q.append([nxt, c[color]])
                            else:
                                if visit[nxt] == color:
                                    return 'NO'
        return 'YES'

    print(bfs())