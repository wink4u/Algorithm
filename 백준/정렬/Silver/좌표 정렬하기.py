import sys
input = sys.stdin.readline

arr = []

N = int(input())

for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda x : (x[0], x[1]))

for i in range(N):
    print(*arr[i])