import sys
input = sys.stdin.readline

n = int(input())

check = input().strip()
f, e = check.split('*')
f_len, e_len = len(f), len(e)

for _ in range(n):
    s = input().strip()
    flag = 0

    if len(s) < f_len + e_len:
        print('NE')
        continue

    for i in range(f_len):
        if s[i] != f[i]:
            flag = 1
            break

    if flag == 0:
        for i in range(e_len):
            if s[-e_len + i] != e[i]:
                flag = 1
                break

    if flag:
        print('NE')
    else:
        print('DA')