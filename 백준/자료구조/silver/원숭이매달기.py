import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    maxDepth = 0
    arr = input()
    stack = []

    for string in arr:
        if string == ']':
            maxDepth = max(maxDepth, len(stack))
            stack.pop()
        else:
            stack.append(string)

    print(2 ** maxDepth)