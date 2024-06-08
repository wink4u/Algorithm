import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def check(v, n):
    if n == 1:
        return v % C
    else:
        tmp = check(v, n // 2)
        if n % 2:
            return (tmp * tmp * A) % C
        else:
            return (tmp * tmp) % C

print(check(A, B))
