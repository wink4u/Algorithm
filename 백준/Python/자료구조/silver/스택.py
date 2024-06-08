import sys
input = sys.stdin.readline

N = int(input())

stack = []
for i in range(N):
    command = input().rstrip()

    if len(command) >= 4:
        if command[0:4] == 'push':
            stack.append(command[5:])

        elif command[0:4] == 'size':
            print(len(stack))

        elif command[0:5] == 'empty':
            if len(stack):
                print(0)
            else:
                print(1)

    else:
        if command == 'pop':
            if stack:
                res = stack.pop()
                print(res)
            else:
                print(-1)
        elif command == 'top':
            if stack:
                print(stack[-1])
            else:
                print(-1)