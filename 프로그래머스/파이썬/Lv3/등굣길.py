def solution(m, n, puddles):
    grid = [[0] * (m + 1) for _ in range(n + 1)]
    grid[1][1] = 1
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if [x, y] in puddles:
                continue
            b1 = grid[y - 1][x]
            b2 = grid[y][x - 1]
            if [x, y - 1] in puddles:
                b1 = 0
            if [x - 1, y] in puddles:
                b2 = 0
            grid[y][x] += b1 + b2
    answer = grid[n][m] % 1000000007
    return answer