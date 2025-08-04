import sys
import heapq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    arr = list(map(int, input().split()))
    heapq.heapify(arr)

    res = 0
    while True:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        res += (a + b)

        if len(arr) == 0:
            break

        heapq.heappush(arr, a + b)

    print(res)