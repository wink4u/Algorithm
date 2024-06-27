import sys
input = sys.stdin.readline

N = int(input())

classes = []
for i in range(N):
    s, e = map(int, input().split())
    classes.append([s, e, e - s])

classes.sort(key = lambda x : (x[1], x[2]))

# print(classes)
start, end = classes[0][0], classes[0][1]
res = 1

# print(classes)

for i in range(1, N):
    ns, ne, tmp = classes[i]

    if ns >= end:
        start = ns
        end = ne
        res += 1

print(res)