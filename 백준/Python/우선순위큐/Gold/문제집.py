import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
node = [[] for _ in range(n + 1)]
check = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    check[b] += 1

q = []

for i in range(1, n + 1):
    if not check[i]:
        heapq.heappush(q, i)

ans = []
while q:
    now = heapq.heappop(q)
    ans.append(now)

    for nxt in node[now]:
        check[nxt] -= 1
        if check[nxt] == 0:
            heapq.heappush(q, nxt)

print(*ans)