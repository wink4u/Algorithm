import sys
from collections import defaultdict
input = sys.stdin.readline

move = {'R' : [0, 1], 'L' : [0, -1], 'T' : [1, 0], 'B' : [-1, 0], 'RT' : [1, 1], 'RB' : [-1, 1], 'LT' : [1, -1], 'LB' : [-1, -1]}

king, stone, N = input().split()
kx, ky = int(king[1]), ord(king[0]) - 65
sx, sy = int(stone[1]), ord(stone[0]) - 65

for i in range(int(N)):
    mx, my = move[input().strip()]

    nx = kx + mx
    ny = ky + my

    if 1 <= nx <= 8 and 0 <= ny < 8:
        if nx == sx and ny == sy:
            snx = sx + mx
            sny = sy + my
            if 1 <= snx <= 8 and 0 <= sny < 8:
                kx, ky = nx, ny
                sx, sy = snx, sny
        else:
            kx = nx
            ky = ny

print(chr(ky + 65) + str(kx))
print(chr(sy + 65) + str(sx))