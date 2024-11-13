from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    node = [[] for _ in range(n + 1)]

    for a, b in roads:
        node[a].append(b)
        node[b].append(a)

    visit = [0] * (n + 1)
    res = [1e8] * (n + 1)

    d = destination

    visit[d] = 1
    res[d] = 0

    q = deque()
    q.append(d)

    while q:
        now = q.popleft()

        for nxt in node[now]:
            if not visit[nxt]:
                res[nxt] = res[now] + 1
                visit[nxt] = 1
                q.append(nxt)

    for i in range(len(sources)):
        s = sources[i]
        if res[s] == 1e8:
            answer.append(-1)
        else:
            answer.append(res[s])

    return answer