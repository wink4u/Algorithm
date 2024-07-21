import sys
import copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline

# 0 은 빈칸, 1은 벽, 2는 바이러스
zero = []
birus = []

N, M = map(int, input().split())
arr = []
zero_cnt = -3

for i in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

    for j in range(M):
        if tmp[j] == 0:
            zero.append([i, j])
            zero_cnt += 1
        elif tmp[j] == 2:
            birus.append([i, j])

com = list(combinations(zero, 3))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = 0

def bfs(wall, b, cnt):
    global res

    copy_arr = copy.deepcopy(arr)

    visit = [[0] * M for _ in range(N)]
    for bx, by in b:
        visit[bx][by] = 1

    q = deque(b)

    for wx, wy in wall:
        copy_arr[wx][wy] = 1

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
                if copy_arr[nx][ny] == 0:
                    q.append([nx, ny])
                    visit[nx][ny] = 1
                    cnt -= 1

                    if res > cnt:
                        return 0

    return cnt

for c in com:
    ans = bfs(c, birus, zero_cnt)
    res = max(res, ans)

print(res)
