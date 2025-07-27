import sys
input = sys.stdin.readline

n = int(input())
arr = []
res = -1e9

for i in range(n):
    tmp = list(map(int, input().split()))
    res = max(res, max(tmp))
    tmp = [0] + tmp
    for j in range(1, n + 1):
        tmp[j] += tmp[j - 1]
    arr.append(tmp)

for k in range(2, n + 1):
    for i in range(k, n + 1):
        test = []
        for j in range(n):
            test.append(arr[j][i] - arr[j][i - k])
        for j in range(n - k + 1):
            res = max(res, sum(test[j:j+k]))

print(res)