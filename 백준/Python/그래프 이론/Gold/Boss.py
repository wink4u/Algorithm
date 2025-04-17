import sys
from collections import deque, defaultdict

input = sys.stdin.readline

# 직원수, 직속 상관 관계 수, 지시 수
n, m, h = map(int, input().split())
coworker = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[y].append(x)

worker = defaultdict(int)
for i in range(1, n + 1):
    worker[i] = i


# print(graph)

def find(k, res):
    if worker[k] == res:
        return k
    else:
        return find(worker[k], res)


# print(graph)
ans = []
for _ in range(h):
    c = list(input().split())

    if c[0] == 'T':
        c[1], c[2] = int(c[1]), int(c[2])
        # 위치 바꿔주기
        r1, r2 = find(c[1], c[1]), find(c[2], c[2])
        worker[r1] = c[2]
        worker[r2] = c[1]
    else:
        c[1] = int(c[1])
        visit = [0] * (n + 1)
        q = deque()
        # 사람의 위치에서 시작
        node = find(c[1], c[1])
        visit[node] = 1
        q.append(node)
        _min = 1e8

        while q:
            now = q.popleft()
            for nxt in graph[now]:
                if not visit[nxt]:
                    visit[nxt] = 1
                    _min = min(_min, coworker[worker[nxt]])
                    q.append(nxt)
        print(_min if _min != 1e8 else '*')
