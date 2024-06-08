import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    gwalho = input().rstrip()

    res = []
    for check in gwalho:
        if check == '(':
            res.append(check)
        else:
            if res:
                if res[-1] == '(':
                    res.pop()
            else:
                res.append(check)

    if res:
        print('NO')
    else:
        print('YES')