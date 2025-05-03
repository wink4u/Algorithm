import sys
input = sys.stdin.readline

n, q = map(int, input().split())

visit = [0 for i in range(n + 1)]


for _ in range(q):
    num = int(input())

    k = num
    check = []

    while k != 1:
        if visit[k]:
            check.append(k)
        k //= 2

    if check:
        print(check[-1])
    else:
        print(0)
        visit[num] = 1

