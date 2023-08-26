import sys
input = sys.stdin.readline

# 테스트 케이스
T = int(input())

DP = [0, 1, 2, 4]


for i in range(4, 11):
    ans = DP[i-1] + DP[i - 2] + DP[i - 3]
    DP.append(ans)

for i in range(T):
    N = int(input())
    print(DP[N])