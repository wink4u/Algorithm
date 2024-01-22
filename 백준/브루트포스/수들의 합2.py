import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0

left = 0
right = 1

while right <= N and left <= right:

    res = sum(nums[left:right])

    if res == M:
        cnt += 1
        right += 1
    elif res < M:
        right += 1
    else:
        left += 1

print(cnt)
