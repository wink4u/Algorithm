import sys
input = sys.stdin.readline

n, k = map(int, input().split())
battery = list(map(int, input().split()))

_max = sum(battery)

DP = [0] * (_max + 1)

for i in range(len(battery)):
    for j in range(_max - battery[i], 0, -1):
        if 0 < DP[j] < k:
            if DP[j + battery[i]] != 0 and DP[j + battery[i]] <= DP[j] + 1:
                continue
            DP[j + battery[i]] = DP[j] + 1
    DP[battery[i]] = 1


cnt = 0
ans = []

for i in range(len(DP)):
    if DP[i]:
        cnt += 1
        ans.append(i)
print(cnt)
print(*ans)