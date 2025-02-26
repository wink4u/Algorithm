import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
new_arr = [0] * (n + 1)

for i in range(1, n + 1):
    new_arr[i] += new_arr[i - 1] + arr[i - 1]

check = []

for i in range(1, n + 1):
    check.append(new_arr[i] - new_arr[0])

check.sort(reverse= True)
res = 0

for i in range(k):
    res += check[i]

print(res)