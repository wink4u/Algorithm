import sys
input = sys.stdin.readline

N, M = map(int, input().split())


def check(value):
    for i in range(2, int(value ** (1 / 2)) + 1):
        if value % i == 0:
            return False

    return True


for i in range(N, M + 1):
    if i == 1:
        continue

    if check(i) == True:
        print(i)
