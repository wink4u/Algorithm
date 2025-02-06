import sys
input = sys.stdin.readline

# 처음 바이러스의 수, 증가율, 총 시간
K, P, N = map(int, input().split())

# 원래 오답
# P, K 의 값은 최대 10의 8승으로
# 메모리적으로 큰 값을 가질 수 있기에 오답이 나옴
# print(K * (P ** N))

# 그러기에 N시간동안 K의 증가된 값을 미리 처리해서 구현
for i in range(N):
    K *= P
    if K >= 1000000007:
        K %= 1000000007

print(K)

