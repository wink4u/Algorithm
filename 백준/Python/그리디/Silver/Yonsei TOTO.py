import sys
input = sys.stdin.readline

n, m = map(int, input().split())

res = []
for _ in range(n):
    p, l = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse= True)
    if l > p:
        res.append(1)
    else:
        res.append(arr[l - 1])


res.sort()
cnt = 0
_sum = 0
for i in range(n):
    _sum += res[i]
    if _sum > m:
        break
    cnt += 1

print(cnt)