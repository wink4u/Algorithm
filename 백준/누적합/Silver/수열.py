import sys
input = sys.stdin.readline

N, K = map(int, input().split())

num = list(map(int, input().split()))
arr = [0, num[0]]
for i in range(1, N):
    total = arr[i] + num[i]
    arr.append(total)

res = -100 * K

for i in range(K, len(arr)):
    res = max(res, arr[i] - arr[i - K])

print(res)