import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    print(3)
else:
    arr.sort(reverse = True)

    res = []

    for i in range(1, n):
        res.append(arr[i] + i + 1)

    print(max(res) + 1)