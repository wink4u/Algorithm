import sys
input = sys.stdin.readline

g = int(input())
x, y = 2, 1
ans = []

while x > y:
    if (x ** 2) - (y ** 2) > g:
        y += 1
    else:
        if (x ** 2) - (y ** 2) == g:
            ans.append(x)

        if x == 1e6:
            y += 1
        else:
            x += 1

if ans:
    for a in ans:
        print(a)
else:
    print(-1)