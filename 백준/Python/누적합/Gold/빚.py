import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    n = arr[0]
    arr[0] = 0
    arr.sort()
    check = arr[:]
    for i in range(1, n + 1):
        check[i] += check[i - 1]

    ans = 0
    for i in range(2, n + 1):
        res = 1e11
        for j in range(i, n + 1):
            res = min(res, arr[j] * i - (check[j] - check[j - i]))
        ans += res

    print(ans)
