import sys

input = sys.stdin.readline

n, m = map(int, input().split())

c = []

for _ in range(n):
    a, b = input().split()
    c.append([a, int(b)])

c.sort(key=lambda x: x[1])

for _ in range(m):
    num = int(input())
    L, R = 0, len(c) - 1

    while L <= R:
        mid = (L + R) // 2

        if num <= c[mid][1]:
            R = mid - 1
        else:
            L = mid + 1

    print(c[L][0])