import sys

input = sys.stdin.readline

while True:
    n = int(input())

    if n == 0:
        break

    if n <= 9:
        print(n)
        continue

    num = 1
    count = 9

    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    while True:
        str_num = str(num)
        flag = 0
        for i in range(10):
            if nums[i] not in str_num:
                count += 1
                if count == n:
                    print(str_num + nums[i])
                    flag = 1
                    break

        if flag:
            break

        num += 1
