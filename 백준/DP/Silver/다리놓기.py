import sys
input = sys.stdin.readline

# 강의 서쪽에는 N개의 사이트
# 강의 동쪽에는 M개의 사이트 N <= M

# 테스트케이스 수 T
T = int(input())

for i in range(T):
    N, M = map(int,input().split())
    if N == 1:
        print(M)
    else:
        DP = []
        DP.append((1, 1))

        first = M
        second = 1
        for i in range(2, N + 1):
            M -= 1
            first *= M
            second *= i
            DP.append((first, second))


        print(round(DP[N - 1][0] / DP[N - 1][1]))
