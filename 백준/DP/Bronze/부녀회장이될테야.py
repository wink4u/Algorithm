import sys
input = sys.stdin.readline

# 테스트 케이스 T

T = int(input())

# 조건
# k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력

# a층의 b호에 사려고
# a-1층의 1호 부터 b호까지 사람들의 수의 합만큼 데려와야함

# 아파트는 0층부터 있고 각층에는 1호부터 있고 i호에는 i명
for i in range(T):
    n = int(input())
    k = int(input())

    DP = [i for i in range(k + 1)]

    for j in range(n):
        for t in range(1, k + 1):
            DP[t] += DP[t - 1]

    print(DP[k])
