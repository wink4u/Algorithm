import sys, math
input = sys.stdin.readline

N = int(input())

water = list(map(int, input().split()))

value = 99999999999999

a_l, a_r = 0, 0

for i in range(N - 1):
    now = water[i]

    start = i + 1
    end = N - 1

    while start <= end:
        mid = (start + end) // 2
        tmp = now + water[mid]

        if abs(tmp) < value:
            value = abs(tmp)
            a_l = i
            a_r = mid

            if tmp == 0:
                break

        if tmp < 0:
            start = mid + 1
        else:
            end = mid - 1

print(water[a_l], water[a_r])


