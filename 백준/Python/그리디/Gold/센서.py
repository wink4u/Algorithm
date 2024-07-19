import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

if K >= N:
    print(0)
    exit()

arr = list(map(int, input().split()))
arr.sort()

dist = []
for i in range(1, N):
    dist.append(arr[i] - arr[i - 1])

dist.sort()
for i in range(K - 1):
    dist.pop()

print(sum(dist))