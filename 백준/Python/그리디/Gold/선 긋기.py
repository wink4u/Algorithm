import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

res = 0

s, e = arr[0]

for st, end in arr[1:]:
    if st > e:
        res += e - s
        s = st
    e = max(end, e)

res += e - s
print(res)
