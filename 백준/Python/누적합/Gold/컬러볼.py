import sys
input = sys.stdin.readline

# 자기 공보다 크기가 작고 색이 다른 공을 잡는다

n = int(input())
check = []
res = [0] * n
color = [0] * (n + 1)

for i in range(n):
    c, v = map(int, input().split())
    check.append([c, v, i])

check.sort(key = lambda x: (x[1], x[0]))
j = 0
total = 0

for i in range(n):
    while check[j][1] < check[i][1]:
        color[check[j][0]] += check[j][1]
        total += check[j][1]
        j += 1

    res[check[i][2]] = total - color[check[i][0]]


for i in range(n):
    print(res[i])