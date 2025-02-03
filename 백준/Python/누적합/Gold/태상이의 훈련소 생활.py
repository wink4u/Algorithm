import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

check = [0 for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())

    check[a - 1] += c
    check[b] -= c


change = 0
for i in range(n):
    change += check[i]
    arr[i] += change

print(*arr)