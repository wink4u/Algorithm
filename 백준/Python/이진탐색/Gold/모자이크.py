import sys
input = sys.stdin.readline

n, m = map(int, input().split())
count = int(input())
paper = int(input())

mx, y_list = 0, []

for _ in range(paper):
    x, y = map(int, input().split())
    mx = max(mx, x)
    y_list.append(y)

y_list.sort()

def count_paper(value):
    cnt = 1
    prev = y_list[0]
    if len(y_list) > 1:
        for k in y_list:
            if prev + value <= k:
                prev = k
                cnt += 1

    return cnt


left, right = mx, 10 ** 7
ans = 10 ** 7

while left <= right:
    mid = (left + right) // 2
    pc = count_paper(mid)

    if pc <= count:
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1

print(ans)