import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
res = [0 for _ in range(N)]
stack = []

for i in range(N - 1, -1, -1):
    now = num[i]

    if len(stack) == 0:
        res[i] = -1
        stack.append(now)
        continue

    top = stack[-1]

    if now < top:
        res[i] = top
    else:
        while True:
            if len(stack) != 0 and stack[-1] <= now:
                stack.pop()
            else:
                break

        if len(stack) == 0:
            res[i] = -1
        else:
            res[i] = stack[-1]

    stack.append(now)


print(*res)