import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
res = [0] * 4

for _ in range(k):
    x, y = map(int, input().split())

    if x % 2:
        if (x + y) % 2:
            res[0] = 1
        else:
            res[1] = 1
    else:
        if (x + y) % 2:
            res[2] = 1
        else:
            res[3] = 1


print('YES' if sum(res) == 4 else 'NO')