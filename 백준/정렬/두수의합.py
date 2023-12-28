import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
mokpyo = int(input())

numbers.sort()

count = 0
start = 0
end = N - 1

while start < end:
    ans = numbers[start] + numbers[end]

    if ans == mokpyo:
        count += 1
        start += 1
    elif ans > mokpyo:
        end -= 1
    else:
        start += 1

print(count)
