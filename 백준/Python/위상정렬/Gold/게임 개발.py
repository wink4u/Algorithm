import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
node = [[] for _ in range(n + 1)]
# 선입간선 개수
check = [0] * (n + 1)
# i 번째 건물의 건설 시간
value = [0] * (n + 1)

for i in range(1, n + 1):
    tmp = list(map(int, input().split()))
    value[i] = tmp[0]

    for t in tmp[1:-1]:
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
        # 건설할때 현재 건설된 시간과, 이전 건물의 짓는시간 + 현재 건물 소요 시간 비교
        dp[nxt] = max(dp[nxt], dp[now] + value[nxt])

for i in dp[1:]:
    print(i)