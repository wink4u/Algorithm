import sys
input = sys.stdin.readline

boards = input().strip() + 'T'

cnt = 0
res = []
flag = 0

for i in range(len(boards)):
    if boards[i] == 'X':
        cnt += 1
    else:
        if cnt % 2:
            flag = 1
            break
        else:
            while cnt:
                if cnt > 2:
                    res.append('AAAA')
                    cnt -= 4
                else:
                    res.append('BB')
                    cnt -= 2

            if boards[i] == '.':
                res.append('.')

if flag:
    print(-1)
else:
    print(''.join(res))