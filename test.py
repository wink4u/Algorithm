import sys
input = sys.stdin.readline

N = int(input())

fruits = list(map(int, input().split()))
nums = [0 for _ in range(10)]

L, R = 0, 0
_max = 0
cnt = 0
kind = 0
while True:
    if R >= N:
        break

    if nums[fruits[R]] == 0:
        kind += 1

    cnt += 1
    nums[fruits[R]] += 1

    if kind > 2:
        if nums[fruits[L]] == 1:
            kind -= 1

        nums[fruits[L]] -= 1
        cnt -= 1
        L += 1

    _max = max(_max, cnt)
    R += 1

print(_max)