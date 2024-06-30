import sys

input = sys.stdin.readline

N = int(input())
nums = []
count = set()

for _ in range(N):
    tmp = int(input())
    nums.append(tmp)
    count.add(tmp)

count = list(count)

_max = 0
for i in range(len(count)):
    n = count[i]
    cnt = 0
    prev = 0
    for j in range(len(nums)):
        if nums[j] == n:
            continue

        if cnt == 0:
            prev = nums[j]
            cnt = 1
        else:
            if prev == nums[j]:
                cnt += 1
            else:
                _max = max(_max, cnt)
                prev = nums[j]
                cnt = 1

    _max = max(_max, cnt)

print(_max)
