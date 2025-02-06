import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

DP = [1 for _ in range(len(numbers))]

for i in range(1, len(numbers)):
    find = 0
    for j in range(i):
        if numbers[j] < numbers[i]:
            find = max(find, DP[j])
    DP[i] = find + 1


print(max(DP))