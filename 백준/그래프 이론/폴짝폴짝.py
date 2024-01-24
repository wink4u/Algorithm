import sys
from collections import deque
input = sys.stdin.readline

# 징검다리수
N = int(input())

bridge = list(map(int, input().split()))

a, b = map(int, input().split())


def bfs(s):
    q = deque()
    q.append(s)
    visit = [-1] * (N)
    visit[s] = 0
    while q:
        jump = q.popleft()

        for check in range(jump, N, bridge[jump]):
            if visit[check] == -1:
                q.append(check)
                visit[check] = visit[jump] + 1
                if check == b - 1:
                    return visit[check]

        for check in range(jump, -1, -bridge[jump]):
            if visit[check] == -1:
                q.append(check)
                visit[check] = visit[jump] + 1
                if check == b - 1:
                    return visit[check]
    return -1

print(bfs(a - 1))

