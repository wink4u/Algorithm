import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

plus = []

for i in range(n):
    for j in range(i, n):
        plus.append(arr[i] + arr[j])

plus.sort()
res = 0

for i in range(n):
    for j in range(i, n):
        check = arr[j] - arr[i]
        left, right = 0, len(plus) - 1

        while left < right:
            mid = (left + right) // 2

            if plus[mid] > check:
                right = mid - 1
            elif plus[mid] < check:
                left = mid + 1
            else:
                res = max(res, arr[j])
                break

print(res)