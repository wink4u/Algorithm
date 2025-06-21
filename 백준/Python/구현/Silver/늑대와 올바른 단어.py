import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)

flag = 0
arr = [0, 0, 0, 0]
idx = 0

cnt = 0
prev = ''
while idx < n:
    if prev == '':
        if s[idx] == 'w':
            prev = 'w'
            arr[0] += 1
        else:
            flag = 1
            break
    elif prev == 'w':
        if s[idx] == 'w':
            arr[0] += 1
        elif s[idx] == 'o':
            prev = 'o'
            arr[1] += 1
        else:
            flag = 1
            break
    elif prev == 'o':
        if s[idx] == 'o':
            arr[1] += 1
        elif s[idx] == 'l':
            prev = 'l'
            arr[2] += 1
        else:
            flag = 1
            break
    elif prev == 'l':
        if s[idx] == 'l':
            arr[2] += 1
        elif s[idx] == 'f':
            prev = 'f'
            arr[3] += 1
        else:
            flag = 1
            break
    elif prev == 'f':
        if s[idx] == 'f':
            arr[3] += 1
        elif s[idx] == 'w':
            cnt = arr[0]
            flag2 = 0
            for i in range(1, 4):
                if arr[i] != cnt:
                    flag2 = 1
                    break
            if flag2:
                flag = 1
                break

            prev = 'w'
            arr = [0, 0, 0, 0]
            arr[0] += 1
        else:
            flag = 1
            break
    idx += 1


for i in range(1, 4):
    if arr[i] != arr[i - 1]:
        flag = 1
        break

if flag:
    print(0)
else:
    print(1)
