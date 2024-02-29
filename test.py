import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temp = list(map(int, input().split()))

if K > N:
    K = N

chips = []

for i in range(N):
    chips.append([i, temp[i]])

res = [0] * N
sorted_chips = sorted(chips, key = lambda x : (-x[1], x[0]))
connect = []

for k in range(K):
    # if k < N:  # 전원선 수가 부품 수보다 클 수 있으므로 확인
    connect.append(sorted_chips[k][0] + 1)
    res[sorted_chips[k][0]] = sorted_chips[k][0] + 1

for i in range(len(connect)):
    print(connect[i])

for i in range(N):
    print(res[i])