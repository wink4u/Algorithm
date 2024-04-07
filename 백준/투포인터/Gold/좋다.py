import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
num.sort()

ans = 0

for i in range(N):
    value = num[i]

    tmp = num[:i] + num[i + 1:]
    left, right = 0, len(tmp) - 1

    while left < right:
        res = tmp[left] + tmp[right]

        if res == value:
            ans += 1
            break

        elif res < value:
            left += 1
        else:
            right -= 1

print(ans)