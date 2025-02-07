import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
jew = [list(map(int, input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]
jew.sort()
bag.sort()
ans = 0

tmp = []
for i in range(len(bag)):
    weight = bag[i]
    while jew and jew[0][0] <= weight:
        heapq.heappush(tmp, -jew[0][1])
        heapq.heappop(jew)

    if tmp:
        ans -= heapq.heappop(tmp)

print(ans)