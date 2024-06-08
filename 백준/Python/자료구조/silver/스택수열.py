import sys
input = sys.stdin.readline

N = int(input())

start = int(input())
arr = []

res = []
num = 1

for i in range(start):
    arr.append(num)
    res.append('+')
    num += 1

arr.pop()
res.append('-')

for i in range(N - 1):
    next = int(input())
    flag = 0

    if num > next:
        while True:
            if arr:
                tmp = arr.pop()
                res.append('-')
                if tmp == next:
                    break

            if len(arr) == 0:
                flag = 1
                break
    else:
        while True:
            arr.append(num)
            res.append('+')
            if num == next:
                num += 1
                arr.pop()
                res.append('-')
                break

            num += 1
            if num > N:
                flag = 1
                break

    if flag == 1:
        print('NO')
        exit()

for i in range(len(res)):
    print(res[i])

