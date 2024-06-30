import sys

input = sys.stdin.readline

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

M = int(input())
res = []
for _ in range(M):
    res.append(int(input()))

res.sort()

ans = []

for i in range(N - M + 1):
    check = []
    for j in range(i, i + M):
        check.append(nums[j])

    check.sort()

    discount = check[0] - res[0]
    flag = 1
    for j in range(1, M):
        if check[j] - res[j] != discount:
            flag = 0
            break

    if flag:
        ans.append(i + 1)

print(len(ans))
for i in range(len(ans)):
    print(ans[i])