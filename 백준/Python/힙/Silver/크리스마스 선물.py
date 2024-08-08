import sys
import heapq
input = sys.stdin.readline

n = int(input())

gift = []

for _ in range(n):
    k = list(map(int, input().split()))
    if k[0]:
        for i in range(1, k[0] + 1):
            heapq.heappush(gift, -k[i])
    else:
        if gift:
            tmp = heapq.heappop(gift)
            print(-tmp)
        else:
            print(-1)
