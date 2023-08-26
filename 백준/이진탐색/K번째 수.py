import sys
input = sys.stdin.readline

N = int(input())

arr = []

for i in range(1, N + 1):
    temp = []
    for j in range(1, N + 1):
        temp.append(i * j)

    arr.append(temp)

print(arr)
