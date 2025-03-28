import sys
input = sys.stdin.readline

s = list(input().strip())
left_cnt, right_cnt = [], []

# K의 개수를 세서 각 R의 자리에 넣어줌
cnt = 0
for i in s:
    if i == 'K':
        cnt += 1
    else:
        left_cnt.append(cnt)

cnt = 0
for i in s[::-1]:
    if i == 'K':
        cnt += 1
    else:
        right_cnt.append(cnt)

right_cnt.reverse()

left = 0
right = len(right_cnt) - 1
ans = 0

while left <= right:
    ans = max(ans, right - left + 1 + min(left_cnt[left], right_cnt[right]) * 2)

    if left_cnt[left] < right_cnt[right]:
        left += 1
    elif left_cnt[left] > right_cnt[right]:
        right -= 1
    else:
        left += 1
        right -= 1

print(ans)