import sys
input = sys.stdin.readline

N = int(input())

M = int(input())

S = input().strip()
flag = 0

prev = ''
cnt = 0
res = 0
for i in range(M):
    if flag == 0:
        if S[i] == 'I':
            flag = 1
            prev = 'I'
    else:
        if prev == 'I':
            if S[i] == 'O':
                prev = 'O'
            else:
                PREV = 'I'
                if cnt >= N:
                    res += cnt - N + 1
                cnt = 0
        else:
            if S[i] == 'I':
                prev = 'I'
                cnt += 1
            else:
                flag = 0
                if cnt >= N:
                    res += cnt - N + 1
                cnt = 0

if cnt >= N:
    res += cnt - N + 1

print(res)