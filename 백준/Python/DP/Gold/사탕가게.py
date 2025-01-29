import sys
input = sys.stdin.readline

while True:
    n, t = input().split()

    if n == '0' and t == '0.00':
        break

    n = int(n)
    t = t.split('.')
    cal = int(t[0]) * 100 + int(t[1])

    arr = []
    for i in range(n):
        v, c = input().split()
        c = c.split('.')
        arr.append([int(v), int(c[0]) * 100 + int(c[1])])

    dp = [0] * (cal + 1)

    for i in range(n):
        value, now = arr[i]
        for j in range(now, cal + 1):
            dp[j] = max(dp[j], dp[j - now] + value)

    print(dp[cal])