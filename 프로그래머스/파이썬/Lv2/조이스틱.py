move = 100000


def dfs(idx, v, n, cnt):
    global move
    if sum(v) == n:
        move = min(move, cnt)
        return

    if move < cnt:
        return

    prev_idx = idx - 1
    next_idx = idx + 1

    if prev_idx < 0:
        prev_idx = n - 1
    if next_idx == n:
        next_idx = 0

    if not v[idx]:
        v[idx] = 1
        dfs(prev_idx, v, n, cnt + 1)
        dfs(next_idx, v, n, cnt + 1)
        v[idx] = 0
    else:
        dfs(prev_idx, v, n, cnt + 1)
        dfs(next_idx, v, n, cnt + 1)


def solution(name):
    answer = 0
    n = len(name)

    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

    visit = [0] * n

    for i in range(n):
        if name[i] == 'A':
            visit[i] = 1

    if sum(visit) == n:
        return 0

    visit[0] = 1
    dfs(0, visit, n, 0)

    return answer + move - 1