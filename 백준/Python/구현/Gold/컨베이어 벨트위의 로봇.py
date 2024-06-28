import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
arr = deque(list(map(int, input().split())))
res = 0
visit = deque([False] * n)

while True:
    res += 1

    arr.rotate(1)
    visit.rotate(1)

    visit[n - 1] = False

    for i in range(n - 2, -1, -1):
        if visit[i] and not visit[i + 1] and arr[i + 1] > 0:
            visit[i], visit[i + 1] = False, True
            arr[i + 1] -= 1

    visit[n - 1] = False

    if arr[0] > 0:
        visit[0] = True
        arr[0] -= 1

    if arr.count(0) >= k:
        break

print(res)