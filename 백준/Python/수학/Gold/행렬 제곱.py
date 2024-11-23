import sys
input = sys.stdin.readline

n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

def shake(arr1, arr2):
    res = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            t = 0
            for k in range(n):
                t += arr1[i][k] * arr2[k][j]

            res[i][j] = t % 1000

    return res

def check(ans, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                ans[i][j] %= 1000

        return ans

    tmp = check(ans, b // 2)

    if b % 2:
        return shake(shake(tmp, tmp), ans)
    else:
        return shake(tmp, tmp)
    # 0 0 = 0 0 * 0 0 + 1 0 * 0 1
    # 1 0 = 1 0 * 0 0 + 1 1 * 1 0
    # 0 1 = 0 1 * 1 1 + 0 0 * 0 1
    # 1 1 = 1 1 * 1 1 + 1 0 * 0 1

answer = check(a, b)

for i in answer:
    print(*i)