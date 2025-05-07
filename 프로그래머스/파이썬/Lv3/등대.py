import sys
sys.setrecursionlimit(10 ** 8)

def solution(n, lighthouse):
    answer = 0
    dp = [[0, 0] for _ in range(n + 1)]
    node = [[] for _ in range(n + 1)]

    for a, b in lighthouse:
        node[a].append(b)
        node[b].append(a)

    visit = [0] * (n + 1)

    def dfs(x):
        visit[x] = True
        dp[x][0] = 0
        dp[x][1] = 1

        for i in node[x]:
            if not visit[i]:
                dfs(i)
                dp[x][0] += dp[i][1]
                dp[x][1] += min(dp[i][0], dp[i][1])

    dfs(1)

    return min(dp[1][0], dp[1][1])