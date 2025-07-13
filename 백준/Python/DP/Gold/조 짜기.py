import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(n):
    dp[i + 1] = dp[i]
    _min = _max = arr[i]
    j = i - 1
    while j >= 0 and (arr[j] < _min or arr[j] > _max):
        _min, _max = min(arr[j], _min), max(arr[j], _max)
        dp[i + 1] = max(dp[i + 1], dp[j] + _max - _min)
        j -= 1

print(dp[-1])