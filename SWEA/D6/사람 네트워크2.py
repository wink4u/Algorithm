import sys
import heapq
sys.stdin = open('test.txt')
input = sys.stdin.readline

t = int(input())

for num in range(t):
    tmp = list(map(int, input().split()))
    n = tmp[0]
    idx = 1
    node = []
    for i in range(n):
        node.append(tmp[idx : idx + n])
        idx += n

    ans = 1e12

    DP = [[1e11] * n for _ in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    DP[i][j] = 0
                    continue

                if node[i][j]:
                    DP[i][j] = 1
                else:
                    DP[i][j] = min(DP[i][j], DP[i][k] + DP[k][j])

    for i in range(n):
        ans = min(ans, sum(DP[i]))

    print(f'#{num + 1} {ans}')