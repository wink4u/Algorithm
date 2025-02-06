import sys
from itertools import product

input = sys.stdin.readline

N, M = map(int, input().split())

# 밭의 정보
board = [list(map(int, input().split())) for _ in range(N)]
# 친구들의 좌표

friends = []
for i in range(M):
    fx, fy = map(int, input().split())
    friends.append([fx - 1, fy - 1])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

_max = 0


def check(path, x, y, route):
    if len(path) == 4:
        route.append(path[:])
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < N and [nx, ny] not in path:
            path.append([nx, ny])
            check(path, nx, ny, route)
            path.pop()


def total(routes):
    res = 0
    visit = set()
    for route in routes:
        for x, y in route:
            if (x, y) in visit:
                return 0
            visit.add((x, y))
            res += board[x][y]
    return res


test = []
for i in range(M):
    routes = []
    check([friends[i]], friends[i][0], friends[i][1], routes)
    test.append(routes)

for comb in product(*test):
    # print(comb)
    _max = max(_max, total(comb))

print(_max)