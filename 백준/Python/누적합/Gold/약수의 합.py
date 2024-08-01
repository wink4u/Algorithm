import sys
input = sys.stdin.readline

T = int(input())

_max = 1000000
tmp = [1] * (_max + 1)
res = [0] * (_max + 1)
res[1] = 1

for i in range(2, _max + 1):
    for j in range(1, (_max // i) + 1):
        tmp[j * i] += i

    res[i] = res[i - 1] + tmp[i]

for _ in range(T):
    N = int(input())
    print(res[N])