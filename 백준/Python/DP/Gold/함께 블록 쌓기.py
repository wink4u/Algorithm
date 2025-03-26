import sys
from collections import defaultdict
input = sys.stdin.readline

n, m, h = map(int, input().split())
dp = [0] * (h + 1)

for i in range(n):
    student = list(map(int, input().split()))
    student.sort(reverse= True)

    tmp = defaultdict(int)

    for j in range(len(student)):
        now = student[j]
        if now < h:
            for k in range(h - now, 0, -1):
                if dp[k]:
                    tmp[k + now] += dp[k]

    for s in student:
        dp[s] += 1

    tmp_k = list(tmp.keys())
    for t in tmp_k:
        dp[t] += tmp[t]

print(dp[h] % 10007)