import sys
input = sys.stdin.readline

n = int(input())

arr = [0, 1]

for i in range(2, n + 1):
    value = arr[i - 1] + arr[i - 2]
    arr.append(value)

print(arr[n])