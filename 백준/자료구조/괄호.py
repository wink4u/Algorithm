import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    gwalho = input()

    res = []
    for check in gwalho:
        if check == '(':
            res.append(check)
        else:
            if res:
                res.pop()


    print(res)
    if res:
        print('NO')
    else:
        print('YES')