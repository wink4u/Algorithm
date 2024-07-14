import sys
input = sys.stdin.readline

N = int(input())

_max = [0, 0, 0]
_min = [0, 0, 0]

for i in range(N):
    board = list(map(int, input().split()))
    _min = [board[0] + min(_min[:2]), board[1] + min(_min), board[2] + min(_min[1:])]
    _max = [board[0] + max(_max[:2]), board[1] + max(_max), board[2] + max(_max[1:])]

print(max(_max), min(_min))