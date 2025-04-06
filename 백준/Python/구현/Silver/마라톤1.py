import sys
input = sys.stdin.readline

n = int(input())

px, py = 0, 0
arr = [0]
d = []
for i in range(n):
    x, y = map(int, input().split())
    d.append([x, y])

    if i != 0:
        arr.append(abs(px - x) + abs(py - y))

    px, py = x, y

total = sum(arr)
res = 0

for i in range(2, n):
    check = total - (arr[i] + arr[i - 1])
    if i == 2:
        res = check + (abs(d[i][0] - d[i - 2][0]) + abs(d[i][1] - d[i - 2][1]))
    else:
        res = min(res, check + (abs(d[i][0] - d[i - 2][0]) + abs(d[i][1] - d[i - 2][1])))

print(res)