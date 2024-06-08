import sys
from collections import deque

input = sys.stdin.readline

A, B, C = map(int, input().split())

# A, B 물통은 비어있고 , C 물통은 가득 차 있음.
# min으로 비교하면서 A,B에 담겨있는 물의 값을 비교하면서
# visit배열에 체크하면서 해야함

ans = []

visited = [[0] * (B + 1) for _ in range(A + 1)]
visited[0][0] = 1
q = deque()
q.append((0, 0))

def check(x, y):
    if not visited[x][y]:
        visited[x][y] = 1
        q.append((x, y))


def bfs():

    while q:
        x, y = q.popleft()
        z = C - x - y

        if x == 0:
            ans.append(z)

        water = min(x, B - y)
        check(x - water, y + water)

        water = min(x, C - z)
        check(x - water, y)

        water = min(y, A - x)
        check(x + water, y - water)

        water = min(y, C - z)
        check(x, y - water)

        water = min(z, A - x)
        check(x + water, y)

        water = min(z, B - y)
        check(x, y + water)

    return ans


answer = bfs()
answer.sort()
print(*answer)

