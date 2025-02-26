import sys
input = sys.stdin.readline

s = input().strip()

if s == '0':
    print('W')
    exit()

tmp = []
res = []
flag = 0
idx = 0
for i in range(len(s)):
    k = s[i]

    if k.isdigit():
        tmp.append(k)
    else:
        if k == 'x':
            num = int(''.join(tmp))
            if flag:
                if num // 2 == 1:
                    res.append(f'-xx')
                else:
                    res.append(f'-{num // 2}xx')
            else:
                if num // 2 == 1:
                    res.append(f'xx')
                else:
                    res.append(f'{num // 2}xx')
            idx = i
            tmp = []
            break
        elif k == '-':
            flag = 1

if tmp:
    if s == '1':
        print('x+W')
    elif s == '-1':
        print('-x+W')
    else:
        print(s + 'x' + '+W')
else:
    if idx != len(s) - 1:
        check = s[idx + 1:]
        if check == '+1':
            res.append('+x')
        elif check == '-1':
            res.append('-x')
        else:
            res.append(check + 'x')
    res.append('+W')
    print(''.join(res))