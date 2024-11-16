import sys
import heapq
input = sys.stdin.readline

n = int(input())

left, right = [], []

for i in range(n):
    v = int(input())

    if len(left) == len(right):
        heapq.heappush(left, -v)
    else:
        heapq.heappush(right, v)

    if right and right[0] < -left[0]:
        l_v = heapq.heappop(left)
        r_v = heapq.heappop(right)

        heapq.heappush(left, -r_v)
        heapq.heappush(right, -l_v)

    print(-left[0])