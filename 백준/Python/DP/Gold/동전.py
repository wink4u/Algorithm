import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    DP = [0] * (m + 1)
    DP[0] = 1

    for coin in coins:
        for i in range(m + 1):
            if i >= coin:
                DP[i] += DP[i - coin]

    print(DP[-1])