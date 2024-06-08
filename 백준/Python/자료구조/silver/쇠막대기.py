import sys
input = sys.stdin.readline

cnt = 0
stick = list(input().strip())

stack = []
for i in range(len(stick)):
    now = stick[i]
    if now == "(":
        stack.append(now)
    else:
        if stick[i - 1] == "(":
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1

print(cnt)
