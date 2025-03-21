import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

node = [[] for _ in range(n + 1)]
value = [0] * (n + 1)
check = [0] * (n + 1)

for i in range(1, n + 1):
    arr = list(map(int, input().split()))
    value[i] = arr[0]

    if len(arr) > 2:
        for t in arr[2:]:
            node[t].append(i)
            check[i] += 1

q = deque()
dp = [0] * (n + 1)

for i in range(1, n + 1):
    if check[i] == 0:
        q.append(i)
        dp[i] = value[i]

while q:
    now = q.popleft()

    for nxt in node[now]:
        check[nxt] -= 1
        if check[nxt] == 0:
            q.append(nxt)

        dp[nxt] = max(dp[nxt], dp[now] + value[nxt])

print(max(dp))