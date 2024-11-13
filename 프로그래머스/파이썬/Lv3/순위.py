from collections import deque


def solution(n, results):
    answer = [0 for _ in range(n + 1)]
    node = [[0] * (n + 1) for _ in range(n + 1)]

    for a, b in results:
        node[a][b] = 1

    for k in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                if node[x][y] == 1 or (node[x][k] == 1 and node[k][y] == 1):
                    node[x][y] = 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if node[i][j]:
                answer[i] += 1
                answer[j] += 1

    res = answer.count(n - 1)
    return res