import sys
input = sys.stdin.readline


def DFS(person, flag):
    if flag:
        blue.append(person)
    else:
        red.append(person)
    for hate in node[person]:
        if hate in check:
            check.remove(hate)
            DFS(hate, not flag)

n = int(input())
blue = []
red = []
node = [[]] + [list(map(int, input().split()))[1:] for _ in range(n)]
check = set(range(1, n + 1))
while check:
    c = check.pop()
    DFS(c, True)

blue.sort()
red.sort()
print(len(blue))
print(*blue)
print(len(red))
print(*red)