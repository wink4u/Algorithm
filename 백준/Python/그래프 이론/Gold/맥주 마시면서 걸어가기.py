import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    house = list(map(int, input().split()))
    store = [list(map(int, input().split())) for _ in range(n)]
    festival = list(map(int, input().split()))

    q = deque()
    q.append([house[0], house[1], 20])
    visit = [0] * n
    flag = 0

    while q:
        x, y, cnt = q.popleft()

        if abs(x - festival[0]) + abs(y - festival[1]) <= cnt * 50:
            flag = 1
            break

        for i in range(n):
            if not visit[i]:
                if abs(x - store[i][0]) + abs(y - store[i][1]) <= cnt * 50:
                    visit[i] = 1
                    q.append([store[i][0], store[i][1], 20])

    if flag:
        print('happy')
    else:
        print('sad')