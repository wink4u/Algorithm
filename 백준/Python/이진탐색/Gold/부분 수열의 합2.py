import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = arr[:n//2]
right = arr[n//2:]

left_sum = []
right_sum = []

def dfs(arr, res, idx=0, total=0):
    if idx == len(arr):
        res.append(total)
        return

    dfs(arr, res, idx + 1, total + arr[idx])
    dfs(arr, res, idx + 1, total)

dfs(left, left_sum)
dfs(right, right_sum)

left_sum.sort()
right_sum.sort()

start, end = 0, len(right_sum) - 1
res = 0
while start < len(left_sum) and end >= 0:
    l_v, r_v = left_sum[start], right_sum[end]
    total = l_v + r_v
    if total == s:
        l_cnt = 1
        r_cnt = 1
        start += 1
        end -= 1

        while start < len(left_sum) and left_sum[start] == l_v:
            l_cnt += 1
            start += 1

        while end >= 0 and right_sum[end] == r_v:
            r_cnt += 1
            end -= 1

        res += l_cnt * r_cnt

    elif total < s:
        start += 1
    else:
        end -= 1

if s == 0:
    res -= 1

print(res)