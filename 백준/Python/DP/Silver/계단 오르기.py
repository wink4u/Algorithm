import sys
input = sys.stdin.readline

# 규칙

# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안된다. 시작점 포함 X
# 마지막 도착 계단은 반드시 밟아야 한다.

# 계단의 개수 N
N = int(input())

stairs = [0] * (N + 1)
DP = [0] * (N + 1)

for i in range(1, N + 1):
    stairs[i] = int(input())

if N <= 2:
    print(sum(stairs))
else:
    DP[1] = stairs[1]
    DP[2] = stairs[1] + stairs[2]
    DP[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

    for i in range(4, N + 1):
        DP[i] = max(DP[i - 3] + stairs[i - 1] + stairs[i], DP[i - 2] + stairs[i])

    print(DP[N])