import sys
input = sys.stdin.readline
n, m = map(int, input().split())

check = [0] * (n + 1)

for i in range(n):
    arr = list(map(int, input().split()))
    count = arr.count(1)
    check[i + 1] = count

for i in range(2):
    a, b = map(int, input().split())
    for j in range(a, b + 1):
        if check[j]:
            check[j] -= 1

print(sum(check))