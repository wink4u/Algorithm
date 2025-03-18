import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

left, right = 0, len(arr) - 1
res = 0
while left < right:
    person = (right - left) - 1

    l, r = arr[left], arr[right]

    if l <= r:
        left += 1
    else:
        right -= 1

    res = max(min(l, r) * person, res)

print(res)