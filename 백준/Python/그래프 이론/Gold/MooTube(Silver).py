import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, r = map(int, input().split())
    graph[a].append([b, r])
    graph[b].append([a, r])

visit = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

def bfs(s):
    q = deque()
    visit[s][s] = 1

    for i in range(len(graph[s])):
        q.append([graph[s][i][0], graph[s][i][1]])
        visit[s][graph[s][i][0]] = graph[s][i][1]

    while q:
        node, value = q.popleft()

        for next_node, next_value in graph[node]:
            if not visit[s][next_node]:
                next_value = min(next_value, value)
                visit[s][next_node] = next_value
                q.append([next_node, next_value])

check = [0] * (n + 1)

for _ in range(m):
    k, num = map(int, input().split())
    if not check[num]:
        check[num] = 1
        bfs(num)

    cnt = 0
    for i in range(1, n + 1):
        if visit[num][i] >= k and i != num:
           cnt += 1

    print(cnt)
