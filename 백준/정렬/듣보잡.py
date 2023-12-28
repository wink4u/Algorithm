import sys
input = sys.stdin.readline

N, M = map(int, input().split())

see = {}
for i in range(N):
    temp = input().strip()
    see[temp] = 1

result = []

for i in range(M):
    temp = input().strip()

    if see.get(temp, 0) != 0:
        result.append(temp)

result.sort()
print(len(result))
for i in result:
    print(i)

