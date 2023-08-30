import sys
from collections import deque
from pprint import pprint

input = sys.stdin.readline

# n * n 격자에 나무의 그루 수와 벽의 정보가 주어짐

# 제초제의 경우 k의 볌위만큼 대각선으로 퍼지며
# 벽이 있는 경우 가로막혀서 전파되지 않음

# 네 방향 탐색 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 대각선 탐색
ddx = [-1, -1, 1, 1]
ddy = [-1, 1, -1, 1]

# 격자의 크기 n, 박멸이 진행되는 수 m, 제초제의 확산 범위 k, 제초제가 남아 있는 년 수 c
n, m, k, c = map(int, input().split())

trees = []
wall = []
map_v = []

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == -1:
            wall.append((i, j))
        elif temp[j] > 0:
            trees.append((i, j))

    map_v.append(temp)


# 1년동안 나무 성자, 나무 번식
# 그리고 c년 동안 제초제 년수

# 나무 번식 bfs
def bfs(tree):
    q = deque(tree)
    new_tree = []
    while q:
        x, y = q.popleft()

        tree_cnt = 0
        temp = []
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in wall and (nx, ny) not in tree:
                tree_cnt += 1
                temp.append((nx, ny))
                if ((nx, ny)) not in new_tree:
                    new_tree.append((nx, ny))

        if tree_cnt:
            # print(trash, temp)
            value = map_v[x][y] // tree_cnt
            # if value > 0:
            for i in range(len(temp)):
                tx, ty = temp[i]
                map_v[tx][ty] += value

    # print(new_tree)
    for i in range(len(new_tree)):
        if map_v[new_tree[i][0]][new_tree[i][1]] != 0:
            trees.append(new_tree[i])


# 제초제 작업
def bfs2():
    max_v = 0
    result = []
    mx, my = 0, 0
    for i in range(len(trees)):
        x, y = trees[i]
        total = map_v[x][y]
        temp = [(x, y)]
        for d in range(4):
            for count in range(1, k + 1):
                nx = x + (count * ddx[d])
                ny = y + (count * ddy[d])

                if 0 <= nx < n and 0 <= ny < n:
                    if (nx, ny) in trees:
                        total += map_v[nx][ny]
                        temp.append((nx, ny))
                    elif map_v[nx][ny] == 0:
                        temp.append((nx, ny))
                        break
                    elif map_v[nx][ny] <= -1:
                        break

        if max_v <= total:
            if max_v == total:
                # print(mx, x, my, y)
                if mx > x:
                    mx, my = x, y
                    result = temp
                elif mx == x:
                    if my > y:
                        mx, my = x, y
                        result = temp
            else:
                mx, my = x, y
                max_v = total
                result = temp

    res = 0
    for r in range(len(result)):
        if (result[r][0], result[r][1]) in trees:
            res += map_v[result[r][0]][result[r][1]]
            map_v[result[r][0]][result[r][1]] = -2 * (c + 1)
            trees.remove((result[r][0], result[r][1]))

    return res


# 제초제 년수 체크
cnt = 0
trash = deque()
ans = 0

# print(trees)
# pprint(map_v)
for _ in range(m):
    # 나무 성장
    # print(trees)
    for i in range(len(trees)):
        tree_cnt = 0
        for d in range(4):
            nx = trees[i][0] + dx[d]
            ny = trees[i][1] + dy[d]

            if 0 <= nx < n and 0 <= ny < n and (nx, ny) in trees:
                tree_cnt += 1

        map_v[trees[i][0]][trees[i][1]] += tree_cnt
    print('성장후')
    pprint(map_v)
    # 나무 번식
    bfs(trees)
    print('번식후')
    pprint(map_v)
    # 제초제 작업

    res_bfs2 = bfs2()
    ans += res_bfs2
    print('제초작업')
    pprint(map_v)

    for i in range(n):
        for j in range(n):
            if map_v[i][j] < -1:
                map_v[i][j] += 2


print(ans)