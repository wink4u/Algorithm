import sys
input = sys.stdin.readline

# 자기 공보다 크기가 작고 색이 다른 공을 잡는다

n = int(input())
# 색깔에 대한 총핪 배열
arr = [0] * (n + 1)
# 누적합을 하기 위한 배열
w = [0] * 2002
tmp = []

for i in range(n):
    color, weight = map(int, input().split())
    arr[color] += weight
    w[weight] += weight
    tmp.append([color, weight])

for i in range(1, 2002):
    w[i] += w[i - 1]

for i in range(n):
    c, v = tmp[i]
    print(w[v - 1], arr[c])
    ans = w[v - 1] - arr[c] + v
    print(ans)
    # print(0 if ans < 0 else ans)