def solution(wallpaper):
    N = len(wallpaper)
    M = len(wallpaper[0])

    sx, sy, ex, ey = 51, 51, 0, 0

    for i in range(N):
        for j in range(M):
            if wallpaper[i][j] == '#':
                sx, sy = min(sx, i), min(sy, j)
                ex, ey = max(ex, i + 1), max(ey, j + 1)

    answer = [sx, sy, ex, ey]

    return answer