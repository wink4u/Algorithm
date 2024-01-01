import sys
input = sys.stdin.readline

N = int(input())
water = list(map(int, input().split()))

water.sort()

left = 0
right = N - 1

result = []
ans = 9999999999999

while left < right:
    left_v = water[left]
    right_v = water[right]

    res = left_v + right_v

    if abs(res) < ans:
        ans = abs(res)
        result = [left_v, right_v]

    if res < 0:
        left += 1
    else:
        right -= 1

print(*result)