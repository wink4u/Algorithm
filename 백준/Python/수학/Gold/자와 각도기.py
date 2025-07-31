import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
degrees = list(map(int, input().split()))
visit = [0] * 360
visit[0] = 1
check = list(map(int, input().split()))

q = deque([0])
while q:
    now = q.popleft()

    for degree in degrees:
        left, right = degree - now, degree + now
        if left < 0:
            left += 360
        if right >= 360:
            right -= 360

        if not visit[left]:
            visit[left] = 1
            q.append(left)
        if not visit[right]:
            visit[right] = 1
            q.append(right)

for c in check:
    if visit[c]:
        print('YES')
    else:
        print('NO')