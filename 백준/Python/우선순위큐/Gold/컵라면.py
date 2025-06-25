import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(tuple(map(int, input().split())))

arr.sort()
q = []

for num, value in arr:
    heapq.heappush(q, value)
    if num < len(q):
        heapq.heappop(q)

print(sum(q))