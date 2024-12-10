import sys
input = sys.stdin.readline

n, l, r, x = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0

for i in range(2 << (n - 1)):
    _min = 1e9
    _max = 0
    _sum = 0
    for j in range(n):
        if i & (1 << j):
            _sum += arr[j]
            _min = min(_min, arr[j])
            _max = max(_max, arr[j])

    if l <= _sum <= r and _max - _min >= x:
        answer += 1

print(answer)