import sys
input = sys.stdin.readline

N = int(input())

cities = [list(map(int, input().split())) for _ in range(N)]

_min = 100000002


def check(visit, cnt, total, present, start):
    global _min

    if cnt == N - 1:
        if cities[present][start] != 0:
            _min = min(_min, total + cities[present][start])
        return

    if total > _min:
        return

    for toNext in range(N):
        if cities[present][toNext] != 0 and not visit[toNext]:
            visit[present] = 1
            check(visit, cnt + 1, total + cities[present][toNext], toNext, start)
            visit[present] = 0


for i in range(N):
    arr = [0] * N
    arr[i] = 1
    check(arr, 0, 0, i, i)

print(_min)
