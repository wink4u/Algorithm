import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

computers = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    computers[b].append(a)

res = 0

answer = []

def bfs(s):
    q = deque()
    q.append((s))
    visit = [0 for _ in range(N + 1)]
    visit[s] = 1

    while q:
        current = q.popleft()
        for com in computers[current]:
            if not visit[com]:
                visit[com] = 1
                q.append(com)

    return visit.count(1)

for i in range(1, N + 1):
    check_res = bfs(i)

    if check_res > res:
        answer = []
        answer.append(i)
        res = check_res
    elif check_res == res:
        answer.append(i)

print(*answer)


