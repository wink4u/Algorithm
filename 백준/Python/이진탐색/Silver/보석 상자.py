import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(int(input()))

start = 1
end = max(arr)
answer = 0

while start <= end:
    mid = (start + end) // 2
    _sum = 0

    for i in range(m):
        _sum += arr[i] // mid
        if arr[i] % mid:
            _sum += 1

    if _sum > n:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid

print(answer)