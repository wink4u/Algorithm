import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
# n 아이들수, m 친구들 관계 수, k 울음 소리 공명하기 위한 아이의 수

friends = [0] + list(map(int, input().split()))

candy = []
node = [[] for _ in range(n + 1)]
v = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)
    v[a] = 1
    v[b] = 1

for i in range(1, n + 1):
    if not v[i]:
        candy.append([1, friends[i]])
    elif v[i] == 1:
        v[i] = 2
        cnt = 1
        res = friends[i]
        q = deque()
        q.append(i)

        while q:
            now = q.popleft()

            for nxt in node[now]:
                if v[nxt] == 1:
                    v[nxt] = 2
                    res += friends[nxt]
                    cnt += 1
                    q.append(nxt)

        candy.append([cnt, res])

dp = [0] * k

for i in range(len(candy)):
    count, total = candy[i]
    for j in range(k - 1, count - 1, -1):
        dp[j] = max(dp[j], dp[j - count] + total)

print(max(dp))