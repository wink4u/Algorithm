import sys
input = sys.stdin.readline

N, K = map(int, input().split())


def binary(num):
    bi = bin(num)[::-1]

    if bi.count('1') <= K:
        return -1

    return bi.index('1')

count = 0

while True:
    res = binary(N)
    if res != -1:
        N += 2 ** res
        count += 2 ** res
    else:
        break

print(count)
