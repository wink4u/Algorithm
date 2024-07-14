import sys
input = sys.stdin.readline

N = int(input())

turn = 0

while True:
    if N <= 3:
        if N == 3 or N == 1:
            turn += 1
        elif N == 2:
            turn += 2
        break

    N -= 3
    turn += 1

if turn % 2:
    print('SK')
else:
    print('CY')