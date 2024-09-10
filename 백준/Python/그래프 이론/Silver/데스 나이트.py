import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
r1, c1, r2, c2 = map(int, input().split())


dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

def bfs():
    q = deque()
    q.append((r1, c1))
    visit = set()
    visit.add((r1, c1))

    cnt = 0

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()

            for d in range(6):
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visit:
                    if nx == r2 and ny == c2:
                        return cnt + 1
                    else:
                        visit.add((nx, ny))
                        q.append((nx, ny))

        cnt += 1

    return -1

print(bfs())