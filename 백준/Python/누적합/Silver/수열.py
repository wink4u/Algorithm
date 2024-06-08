import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num = list(map(int, input().split()))
arr = [0, num[0]]
for i in range(1, N):
    total = arr[i] + num[i]
    arr.append(total)

ans = 0
for i in range(1, len(arr)):
    # print(arr[i], ans)
    tmp = ans
    if arr[i] % M == 0:
        ans += 1
        ans += tmp
# for i in range(1, len(arr)):
#     present = arr[i]
#     for j in range(i - 1, -1, -1):
#         now = present - arr[j]
#         if now % M == 0:
#             ans += 1

print(ans)