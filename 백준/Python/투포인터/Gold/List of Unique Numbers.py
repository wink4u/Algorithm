import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
l, r = 0, 0
res = 0
check = [0] * 100001

while l <= r and r < n:
    if not check[arr[r]]:
        check[arr[r]] = 1
        r += 1
        res += r - l
    else:
        while check[arr[r]]:
            check[arr[l]] = 0
            l += 1

print(res)
