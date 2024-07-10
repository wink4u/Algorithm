import sys

input = sys.stdin.readline

s = input().strip()

stack = []
tmp = []
for i in range(len(s)):
    if s[i].isdigit():
        tmp.append(s[i])
    else:
        if s[i] == '(':
            tmp.append(len(tmp) - 1)
            stack.append(tmp)
            tmp = []
        else:
            if tmp:
                tmp_len = len(tmp)
                stack_len = stack[-1].pop()
                multiple = int(stack[-1].pop())

                for j in range(len(tmp)):
                    stack[-1].append(tmp[j])

                stack[-1].append(stack_len + tmp_len * multiple)
                tmp = []
            else:
                last = stack.pop()
                last_len = last[-1]
                stack_len = stack[-1].pop()
                multiple = int(stack[-1][-1])

                for j in range(len(last) - 1):
                    stack[-1].append(last[j])

                stack[-1].append(stack_len + last_len * multiple)

if tmp:
    print(len(tmp))
else:
    print(stack[0][-1])
