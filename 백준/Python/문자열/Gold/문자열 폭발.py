import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

stack = []
tmp = []
flag = 0
room = 0

for s in a:
    if flag:
        if s == b[len(tmp[room])]:
            tmp[room].append(s)
            if len(tmp[room]) == len(b):
                tmp.pop()
                if room:
                    room -= 1
                else:
                    flag = 0
        elif s == b[0]:
            room += 1
            tmp.append([s])
        else:
            tmp.append([s])
            for i in range(len(tmp)):
                wrong = ''.join(tmp[i])
                stack.append(wrong)

            tmp = []
            room = 0
            flag = 0
    else:
        if s == b[0]:
            tmp.append([s])
            if len(b) == 1:
                continue
            flag = 1
        else:
            stack.append(s)

if len(b) != 1:
    if tmp:
        for i in range(len(tmp)):
            wrong = ''.join(tmp[i])
            stack.append(wrong)

if len(stack):
    print(''.join(stack))
else:
    print('FRULA')
