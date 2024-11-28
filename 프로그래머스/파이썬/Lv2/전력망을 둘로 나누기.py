from collections import deque


def solution(n, wires):
    answer = -1
    node = [[] for _ in range(n + 1)]

    result = n

    for a, b in wires:
        node[a].append(b)
        node[b].append(a)

    for i in range(n - 1):
        a, b = wires[i]
        visit = [0] * (n + 1)
        visit[a] = 1
        visit[b] = 2

        q = deque()
        q.append(a)
        flag = 0
        while q:
            now = q.popleft()

            for nxt in node[now]:
                if not visit[nxt]:
                    visit[nxt] = 1
                    q.append(nxt)

        if not flag:
            cnt = visit.count(1)
            result = min(result, abs((n - cnt) - cnt))

    return result