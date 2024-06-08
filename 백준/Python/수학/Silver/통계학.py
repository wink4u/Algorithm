import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())

nums = []
count = defaultdict(int)

for i in range(N):
    num = int(input())
    nums.append(num)
    count[num] += 1


sorted_count = sorted(list(count.items()), key = lambda x : (-x[1], x[0]))

print(round((sum(nums) / N)))

nums.sort()
print(nums[N // 2])

if N == 1:
    print(sorted_count[0][0])
else:
    if sorted_count[0][1] != sorted_count[1][1]:
        print(sorted_count[0][0])
    else:
        print(sorted_count[1][0])

print(max(nums) - min(nums))