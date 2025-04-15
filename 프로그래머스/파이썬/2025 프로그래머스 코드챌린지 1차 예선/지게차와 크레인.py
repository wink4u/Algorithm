from collections import deque


def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    answer = n * m

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    arr = []
    arr.append(['.'] * (m + 2))
    for i in range(n):
        arr.append(list('.' + storage[i].strip() + '.'))
    arr.append(['.'] * (m + 2))

    def check(target):
        q = deque()
        q.append((0, 0))
        visit = [[0] * (m + 2) for _ in range(n + 2)]
        cnt = 0

        alp = []

        while q:
            x, y = q.popleft()

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nx < n + 2 and 0 <= ny < m + 2 and not visit[nx][ny]:
                    if arr[nx][ny] == '.':
                        visit[nx][ny] = 1
                        q.append((nx, ny))
                    elif arr[nx][ny] == target:
                        visit[nx][ny] = 1
                        cnt += 1
                        alp.append((nx, ny))

        for ax, ay in alp:
            arr[ax][ay] = '.'

        return cnt

    for c in requests:
        flag = 0
        if len(c) == 2:
            flag = 1

        if not flag:
            answer -= check(c)
        else:
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if arr[i][j] == c[0]:
                        arr[i][j] = '.'
                        answer -= 1

    return answer