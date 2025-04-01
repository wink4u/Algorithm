import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
node = [[] for _ in range(n + 1)]
dp = [0] * n

for i in range(1, n):
    p = arr[i]
    node[p].append(i)

def dfs(idx):
    check = []

    if node[idx]:
        for nxt in node[idx]:
            dfs(nxt)
            check.append(dp[nxt])

        check.sort(reverse=True)

        check = [check[i] + i + 1 for i in range(len(check))]
        dp[idx] = max(check)

dfs(0)
print(dp[0])