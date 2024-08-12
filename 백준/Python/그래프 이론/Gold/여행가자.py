import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    arr = list(map(int, input().split()))

    for j in range(len(arr)):
        if arr[j]:
            graph[i].append(j + 1)


trip = list(map(int, input().split()))

q = deque()
q.append(trip[0])

visit = [0] * (N + 1)
visit[trip[0]] = 1
while q:
    t = q.popleft()

    for node in graph[t]:
        if not visit[node]:
            visit[node] = 1
            q.append(node)

s_trip = list(set(trip))

flag = 0

for s in s_trip:
    if not visit[s]:
        flag = 1
        break

if flag:
    print('NO')
else:
    print('YES')
