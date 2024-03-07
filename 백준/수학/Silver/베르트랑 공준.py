import sys
input = sys.stdin.readline

check = [0, 0] + [1] * 246913

for i in range(2, 246913):
    if check[i]:
        for j in range(2*i, 246913, i):
            check[j] = 0

while True:
    n = int(input())
    if n == 0:
        break
    tmp = check[n + 1: 2*n + 1]

    print(tmp.count(1))