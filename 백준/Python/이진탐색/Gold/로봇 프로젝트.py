import sys
input = sys.stdin.readline

while True:
    x = input().strip()
    if x == '':
        break
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))

    x = int(x) * (10 ** 7)
    arr.sort()

    l, r = 0, len(arr) - 1
    flag = 0
    while l < r:
        if arr[l] + arr[r] == x:
            flag = 1
            break
        else:
            if arr[l] + arr[r] < x:
                l += 1
            else:
                r -= 1

    if flag:
        print(f'yes {arr[l]} {arr[r]}')
    else:
        print('danger')