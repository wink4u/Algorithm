import sys
input = sys.stdin.readline

N = int(input())

start = 1
res = 3
if N == 1:
    print(res)
else:
    prev = 1
    cnt = 1
    while cnt != N:
        tmp = res
        res = res * 2 + prev
        if res > 9901:
            res %= 9901
        prev = tmp

        cnt += 1
        # print(res, cnt, prev)

    print(res)
