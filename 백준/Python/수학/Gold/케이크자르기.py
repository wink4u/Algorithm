import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(0)
elif n % 2:
    print((n // 2) + 1)
else:
    print(n // 2)

