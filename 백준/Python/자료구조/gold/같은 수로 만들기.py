import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    num = int(input())
    if len(arr) == 0 or arr[-1] != num:
        arr.append(num)

res = 0
while True:
    if len(arr) == 1:
        break

    cur = min(arr)
    idx = arr.index(cur)

    if idx == 0:
        right = arr[idx + 1]
        res += right - cur
        arr.pop(idx)
    elif idx == len(arr) - 1:
        left = arr[idx - 1]
        res += left - cur
        arr.pop(idx)
    else:
        left = arr[idx - 1]
        right = arr[idx + 1]
        res += min(left, right) - cur
        if left == right:
            arr[idx] = left
            arr.pop(idx + 1)
            arr.pop(idx - 1)
            continue

        arr.pop(idx)


print(res)