import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))

    _max = 0
    res = 0
    for i in range(N - 1, -1, -1):
        if nums[i] > _max:
            _max = nums[i]
        else:
            res += _max - nums[i]

    print(res)