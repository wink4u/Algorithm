import sys
input = sys.stdin.readline

n = int(input())
home = [list(map(int, input().split())) for _ in range(n)]
res = 1e9


def check(ha, hb):
    x1, y1, z1 = ha
    x2, y2, z2 = hb

    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)


for i in range(n):
    a, b = 1e9, 1e9
    for j in range(n):
        if i != j:
            value = check(home[i], home[j])

            if a > value:
                b = a
                a = value
            elif b > value:
                b = value

    res = min(res, a + b)

print(res)