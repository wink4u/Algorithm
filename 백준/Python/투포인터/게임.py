import sys
input = sys.stdin.readline

X, Y = map(int, input().split())

Z = Y * 100 // X

left = 0
right = X
res = 0
if Z >= 99:
    print(-1)
else:
    while left <= right:
        mid = (left + right) // 2

        if (Y + mid) * 100 // (X + mid) > Z:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    print(res)