import sys
from collections import defaultdict
input = sys.stdin.readline


stack = []

while True:
    n = int(input())

    if n == 0:
        break

    if n <= len(stack):
        print(stack[n - 1])
    else:
        if stack:
            num = stack[-1] + 1
        else:
            num = 1

        while True:
            dic = defaultdict(int)
            flag = 1
            temp = str(num)

            for i in temp:
                if dic.get(i):
                    flag = 0
                    break
                else:
                    dic[i] += 1


            if flag:
                stack.append(num)


            if len(stack) == n:
                print(num)
                break

            num += 1
