import sys
input = sys.stdin.readline

k = int(input())
a, b, c, d = map(int, input().split())

if a * k + b == c * k + d:
    print(f'Yes {a * k + b}')
else:
    print('No')