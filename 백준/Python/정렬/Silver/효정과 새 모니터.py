import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    w, h = map(int, input().split())
    v = (w ** 2 + h ** 2) ** 0.5
    arr.append([i + 1, v])

arr.sort(key = lambda x : (-x[1], x[0]))

for i in range(n):
    print(arr[i][0])