import sys
input = sys.stdin.readline

s = input().strip()
stack = []
g = []
flag = 0

for i in range(len(s)):
    now = s[i]
    if now == '>':
        g.append(now)
        stack.append(g)
        g = []
        flag = 0
    elif now == '<':
        flag = 1
        if g:
            g.reverse()
            stack.append(g)
            g = []
        g.append(now)
    elif now == ' ':
        if flag:
            g.append(now)
        else:
            if g:
                g.reverse()
                stack.append(g)
                g = []
            stack.append([now])
    else:
        g.append(now)


if g:
    if flag:
        stack.append(g)
    else:
        g.reverse()
        stack.append(g)

answer = ''

for i in range(len(stack)):
    answer += ''.join(stack[i])

print(answer)