import sys
input = sys.stdin.readline

K, P, N = map(int, input().split())
N *= 10

def check(x, y):
    if y == 1:
        return x
    elif y % 2 == 1:
        res = check(x, (y - 1) / 2)
        return res * res * x % 1000000007
    else:
        res = check(x, y / 2)
        return res * res % 1000000007

ans = check(P, N) * K
print(ans % 1000000007)
