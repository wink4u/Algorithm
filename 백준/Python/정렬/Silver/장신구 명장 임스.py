import sys
input = sys.stdin.readline

P, N = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0
for i in range(N):

    if P >= 200:
        break
    P += arr[i]
    cnt += 1
print(cnt)