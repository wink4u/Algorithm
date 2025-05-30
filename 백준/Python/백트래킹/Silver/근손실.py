import sys
input = sys.stdin.readline

n, k = map(int, input().split())
work = list(map(int, input().split()))

visit = [False] * (n + 1)
res = 0
def dfs(now, v, cnt):
    global res
    if cnt == n:
        res += 1
        return

    if now < 500:
        return

    for i in range(n):
        if not v[i]:
            v[i] = True
            dfs(now + work[i] - k, v, cnt + 1)
            v[i] = False


dfs(500, visit, 0)
print(res)