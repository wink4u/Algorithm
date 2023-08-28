import sys
input = sys.stdin.readline

DP = [0 for _ in range(101)]

DP[0] = 1
DP[1] = 1
DP[2] = 1
DP[3] = 2
DP[4] = 2

for i in range(5, 101):
    DP[i] = DP[i - 1] + DP[i - 5]

# 테스트케이스 수 T
T = int(input())

for i in range(T):
    print(DP[int(input()) - 1])