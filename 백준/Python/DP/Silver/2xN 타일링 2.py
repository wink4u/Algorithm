import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(3)

elif n >= 3:
    DP = [0 for _ in range(n + 1)]

    DP[1] = 1
    DP[2] = 3
    for i in range(3, n + 1):
        DP[i] = 2 * DP[i - 2] + DP[i - 1]

    print(DP[n] % 10007)