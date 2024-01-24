import sys
input = sys.stdin.readline

N, truck = map(int, input().split())
M = int(input())

towns = []
for i in range(M):
    A, B, C = map(int, input().split())
    towns.append(([A, B, C]))

towns.sort(key = lambda x : (x[1]))

res = 0
post = [truck] * N

for a, b, value in towns:
    min_value = truck

    for i in range(a, b):
        if min_value > min(post[i], value):
            min_value = min(post[i], value)

    for i in range(a, b):
        post[i] -= min_value

    res += min_value
print(res)