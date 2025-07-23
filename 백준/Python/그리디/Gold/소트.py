import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
s = int(input())

for i in range(n - 1):
    if s == 0:
        break

    _max, idx = arr[i], i

    for j in range(i + 1, min(n, i + 1 + s)):
        if _max < arr[j]:
            _max = arr[j]
            idx = j

    s -= idx - i

    for k in range(idx, i, - 1):
        arr[k] = arr[k - 1]
    arr[i] = _max

print(*arr)