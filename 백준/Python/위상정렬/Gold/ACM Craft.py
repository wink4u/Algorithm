import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    build = [0] + list(map(int, input().split()))

    node = [[] for _ in range(n + 1)]
    check = [0] * (n + 1)

    dp = [0] * (n + 1)

    for _ in range(k):
        x, y = map(int, input().split())
        node[x].append(y)
        check[y] += 1

    w = int(input())
    q = deque()

    for i in range(1, n + 1):
        if check[i] == 0:
            q.append(i)
            dp[i] = build[i]

    while q:
        now = q.popleft()

        for nxt in node[now]:
            check[nxt] -= 1
            if check[nxt] == 0:
                q.append(nxt)

            dp[nxt] = max(dp[nxt], dp[now] + build[nxt])

    print(dp[w])