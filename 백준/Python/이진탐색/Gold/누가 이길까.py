import sys
input = sys.stdin.readline

n, m = map(int, input().split())
hi = list(map(int, input().split()))
arc = list(map(int, input().split()))

arc.sort()
ans = [0, 0, 0]
def check(v):
    l, r = 0, m

    while l < r:
        mid = (l + r) // 2

        if arc[mid] < v:
            l = mid + 1
        else:
            r = mid

    return l


for i in range(n):
    a = hi[i]

    idx = check(a)
    idx2 = check(a + 1)

    ans[2] += idx2 - idx
    ans[1] += m - idx2
    ans[0] += idx

print(*ans)