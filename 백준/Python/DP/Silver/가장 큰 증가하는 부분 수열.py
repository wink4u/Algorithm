import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

visit = [0 for _ in range (N)]
visit[0] = arr[0]
for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            visit[i] = max(visit[i], visit[j] + arr[i])
        else:
            visit[i] = max(visit[i], arr[i])

print(max(visit))