import sys
input = sys.stdin.readline

testcase = int(input())


def binary_search(li, a):
    s, e = 0, len(li)-1
    res = -1
    while s <= e:
        m = (s + e) // 2
        if li[m] < a:
            res = m
            s = m + 1
        else:
            e = m - 1

    return res


for _ in range(testcase):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    cnt = 0

    for a in A:
        cnt += (binary_search(B, a) + 1)

    print(cnt)
