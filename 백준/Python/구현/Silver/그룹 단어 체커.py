import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

for _ in range(n):
    s = input().strip()
    check = [0] * 26
    flag = 1
    prev = -1
    for ss in s:
        v = ord(ss) - 97
        if prev == -1:
            prev = v
        else:
            if prev == v:
                continue
            else:
                if check[v]:
                    flag = 0
                    break
                else:
                    check[prev] = 1
                    prev = v

    if flag:
        cnt += 1

print(cnt)
