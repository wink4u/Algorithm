import sys
input = sys.stdin.readline

n = int(input())

stars = [[' '] * 2 * n for _ in range(n)]

def dfs(i, j, size):
    if size == 3:
        stars[i][j] = '*'
        stars[i + 1][j - 1] = stars[i + 1][j + 1] = '*'
        for k in range(-2, 3):
            stars[i + 2][j + k] = '*'
    else:
        new_size = size // 2
        dfs(i, j, new_size)
        dfs(i + new_size, j - new_size, new_size)
        dfs(i + new_size, j + new_size, new_size)

dfs(0, n - 1, n)
for star in stars:
    print("".join(star))