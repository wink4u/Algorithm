import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
q = []
for i in range(k):
    heapq.heappush(q, (-arr[i], i + 1))

mx = max(arr)
if mx > (n + 1) // 2:
    print(-1)
    sys.exit()

result = []
while q:
    v1, idx1 = heapq.heappop(q)
    result.append(idx1)
    v1 += 1

    if q:
        v2, idx2 = heapq.heappop(q)
        result.append(idx2)
        v2 += 1

        if v2 < 0:
            heapq.heappush(q, (v2, idx2))

    if v1 < 0:
        heapq.heappush(q, (v1, idx1))

print(' '.join(map(str, result)))
